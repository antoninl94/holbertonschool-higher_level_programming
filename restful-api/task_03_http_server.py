#!/usr/bin/python3
"""
This is the ``task_03_http_server`` module
"""
import http.server
import socketserver
import json


class BaseHTTPSubclass(http.server.BaseHTTPRequestHandler):
    """
    This is the ``BaseHTTPSubclass`` subclass,
    inherited from ``BaseHTTPRequestHandler``
    """
    def do_GET(self):
        """
        This function handle GET requests
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            resp = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(resp).encode("utf-8"))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            resp = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.wfile.write(json.dumps(resp).encode("utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000
with socketserver.TCPServer(("", PORT), BaseHTTPSubclass) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
