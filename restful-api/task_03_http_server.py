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
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.send_response(200)
            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == '/data':
            self.send_header("Content-type", "application/json")
            self.end_headers()
            resp = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.wfile.write(json.dumps(resp).encode())
        elif self.path == '/info':
            self.send_header("Content-type", "application/json")
            self.end_headers()
            resp = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.send_response(200)
            self.wfile.write(json.dumps(resp).encode())
        elif self.path == '/status':
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.send_response(200)
            self.wfile.write("Ok".encode())
        else:
            self.send_error(404, "Endpoint not found")


PORT = 8000
Handler = BaseHTTPSubclass

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
