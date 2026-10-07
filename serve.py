#!/usr/bin/env python3
"""FYE12 Chemistry exercises server with progress persistence."""
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

PROGRESS_FILE = Path(__file__).parent / "progress.json"
MATCH_PROGRESS_FILE = Path(__file__).parent / "match_progress.json"
CHEMFALL_PROGRESS_FILE = Path(__file__).parent / "chemfall_progress.json"
SORTLAB_PROGRESS_FILE = Path(__file__).parent / "sortlab_progress.json"
MEMORY_PROGRESS_FILE = Path(__file__).parent / "memory_progress.json"
ELEMENTHUNT_PROGRESS_FILE = Path(__file__).parent / "elementhunt_progress.json"
BALANCE_PROGRESS_FILE = Path(__file__).parent / "balance_progress.json"
DIAGRAM_PROGRESS_FILE = Path(__file__).parent / "diagram_progress.json"
PERIODIC_PROGRESS_FILE = Path(__file__).parent / "periodic_progress.json"
PORT = 8099


class Handler(SimpleHTTPRequestHandler):
    def _serve_json_file(self, filepath):
        try:
            data = filepath.read_text() if filepath.exists() else "{}"
        except Exception:
            data = "{}"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data.encode())

    def do_GET(self):
        if self.path == "/api/progress":
            self._serve_json_file(PROGRESS_FILE)
        elif self.path == "/api/match-progress":
            self._serve_json_file(MATCH_PROGRESS_FILE)
        elif self.path == "/api/chemfall-progress":
            self._serve_json_file(CHEMFALL_PROGRESS_FILE)
        elif self.path == "/api/sortlab-progress":
            self._serve_json_file(SORTLAB_PROGRESS_FILE)
        elif self.path == "/api/memory-progress":
            self._serve_json_file(MEMORY_PROGRESS_FILE)
        elif self.path == "/api/elementhunt-progress":
            self._serve_json_file(ELEMENTHUNT_PROGRESS_FILE)
        elif self.path == "/api/balance-progress":
            self._serve_json_file(BALANCE_PROGRESS_FILE)
        elif self.path == "/api/diagram-progress":
            self._serve_json_file(DIAGRAM_PROGRESS_FILE)
        elif self.path == "/api/periodic-progress":
            self._serve_json_file(PERIODIC_PROGRESS_FILE)
        else:
            super().do_GET()

    def _write_json_file(self, filepath):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            obj = json.loads(body)
        except (json.JSONDecodeError, ValueError):
            self.send_response(400)
            self.end_headers()
            return
        filepath.write_text(json.dumps(obj, indent=2))
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def do_POST(self):
        if self.path == "/api/progress":
            self._write_json_file(PROGRESS_FILE)
        elif self.path == "/api/match-progress":
            self._write_json_file(MATCH_PROGRESS_FILE)
        elif self.path == "/api/chemfall-progress":
            self._write_json_file(CHEMFALL_PROGRESS_FILE)
        elif self.path == "/api/sortlab-progress":
            self._write_json_file(SORTLAB_PROGRESS_FILE)
        elif self.path == "/api/memory-progress":
            self._write_json_file(MEMORY_PROGRESS_FILE)
        elif self.path == "/api/elementhunt-progress":
            self._write_json_file(ELEMENTHUNT_PROGRESS_FILE)
        elif self.path == "/api/balance-progress":
            self._write_json_file(BALANCE_PROGRESS_FILE)
        elif self.path == "/api/diagram-progress":
            self._write_json_file(DIAGRAM_PROGRESS_FILE)
        elif self.path == "/api/periodic-progress":
            self._write_json_file(PERIODIC_PROGRESS_FILE)
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    print(f"Serving on http://localhost:{PORT}")
    server.serve_forever()
