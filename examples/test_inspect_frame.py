"""HTTP contract checks; the model here is a local stub, never a real GPU."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from inspect_frame import PROJECT_ROOT, project_path, request_json


class Handler(BaseHTTPRequestHandler):
    last_request = None
    finish_reason = "stop"

    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path.endswith("/large"):
            data = b" " * (2 * 1024 * 1024 + 1)
        else:
            data = json.dumps({"data": [{"id": "stub-vision"}]}).encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        Handler.last_request = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        observation = {"phase": "unknown", "player_center_1000": None}
        data = json.dumps({
            "choices": [{"message": {"content": json.dumps(observation)},
                         "finish_reason": Handler.finish_reason}],
            "usage": {"prompt_tokens": 100, "completion_tokens": 12, "total_tokens": 112},
        }).encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data)


class ClientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}/v1"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_http_request_and_response_contract(self):
        self.assertEqual(request_json(self.base + "/models")["data"][0]["id"], "stub-vision")
        result = request_json(self.base + "/chat/completions", {"model": "stub-vision"})
        self.assertEqual(result["usage"]["total_tokens"], 112)

    def test_oversized_response_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "larger"):
            request_json(self.base + "/large")

    def test_relative_paths_use_repository_root(self):
        self.assertEqual(project_path("output/result.json"), PROJECT_ROOT / "output/result.json")
        self.assertEqual(project_path(str(PROJECT_ROOT / "input.png")), PROJECT_ROOT / "input.png")

    @unittest.skipUnless(importlib.util.find_spec("PIL"), "Install optional vision requirements")
    def test_archival_image_reports_usage_and_never_becomes_actionable(self):
        examples = Path(__file__).resolve().parent
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "observation.json"
            command = [sys.executable, str(examples / "inspect_frame.py"), "--image", "assets/system-architecture-en.png",
                       "--base-url", self.base, "--out", str(output)]
            subprocess.run(command, check=True, capture_output=True, text=True, cwd=directory)
            result = json.loads(output.read_text())
            self.assertFalse(result["actionable"])
            self.assertIn("archival", result["source"])
            self.assertEqual(result["usage"]["total_tokens"], 112)
            self.assertFalse(Handler.last_request["chat_template_kwargs"]["enable_thinking"])
            blocks = Handler.last_request["messages"][0]["content"]
            self.assertTrue(blocks[1]["image_url"]["url"].startswith("data:image/jpeg;base64,"))
            Handler.finish_reason = "length"
            try:
                output.unlink()
                failed = subprocess.run(command, capture_output=True, text=True, cwd=directory)
                self.assertNotEqual(failed.returncode, 0)
                self.assertFalse(output.exists())
                self.assertIn("token limit", failed.stderr)
            finally:
                Handler.finish_reason = "stop"


if __name__ == "__main__":
    unittest.main()
