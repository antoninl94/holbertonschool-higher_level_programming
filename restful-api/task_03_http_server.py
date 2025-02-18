#!/usr/bin/python3
"""
This is the ``task_03_http_server`` module
"""
import http.server
import socketserver
import json


class BaseHTTPSubclass(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        This function handle GET requests
        """
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello, this is a simple API!".encode())
        if self.path == '/data':
            resp = json.dumps({"name": "John", "age": 30, "city": "New York"})\
                .encode()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(resp)


PORT = 8008
Handler = BaseHTTPSubclass

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
