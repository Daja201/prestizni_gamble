#!/usr/bin/env python3
"""Minimal static server to run gamble.html.

Usage:
    python3 server.py [port]        # defaults to port 6767

Binds to 0.0.0.0 so it is reachable from other devices on your network/host
IP, not just localhost. Camera access (getUserMedia) requires the page be
served over http:// or https:// — opening gamble.html directly via file://
will block it in most browsers, so always run it through this server.
"""
import http.server
import socketserver
import sys
import os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 6767
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    with ReusableTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving gamble.html on all interfaces, port {PORT}")
        print(f"  Local:   http://localhost:{PORT}/gamble.html")
        print(f"  Network: http://<your-server-ip>:{PORT}/gamble.html")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")
