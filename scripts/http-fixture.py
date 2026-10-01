#!/usr/bin/env python3
"""A small web server the Http reference examples can run against.

The examples talk to https://api.example.com, which doesn't exist. Start this server, and
check-outputs.py will send those requests here instead and compare the output as usual:

  python3 scripts/http-fixture.py &
  HTTP_FIXTURE=http://127.0.0.1:8765 python3 scripts/check-outputs.py <page> <file_name>

Stop it afterwards (it runs until killed).
"""

import json, time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def send(self, code, body=b"", ctype="text/plain; charset=utf-8", headers=()):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for k, v in headers: self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)
    def do_GET(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        if u.path == "/weather":
            self.send(200, json.dumps({"city": q.get("city", [""])[0], "current": {"temperature": 21.5}}).encode(), "application/json")
        elif u.path == "/hello": self.send(200, b"Hello from the server")
        elif u.path == "/users/404": self.send(404, b"no such user")
        elif u.path == "/boom": self.send(500, b"oops")
        elif u.path == "/old": self.send(301, b"", headers=[("Location", "/hello")])
        elif u.path == "/slow": time.sleep(2); self.send(200, b"late")
        elif u.path == "/binary": self.send(200, b"\xff\xfe\x00", "application/octet-stream")
        elif u.path == "/notjson": self.send(200, b"just words")
        elif u.path == "/headers": self.send(200, b"x", headers=[("X-Request-Id", "abc123"), ("Set-Cookie", "a=1"), ("Set-Cookie", "b=2")])
        else: self.send(404, b"not found")
    def body(self):
        n = int(self.headers.get("Content-Length", 0)); return self.rfile.read(n)
    def do_POST(self):
        b = self.body()
        info = {"type": self.headers.get("Content-Type"), "body": b.decode("utf-8", "replace"), "agent": self.headers.get("User-Agent")}
        self.send(201, json.dumps(info).encode(), "application/json")
    do_PUT = do_PATCH = do_POST
    def do_DELETE(self): self.send(200, b"deleted")

HTTPServer(("127.0.0.1", 8765), H).serve_forever()
