from http.server import BaseHTTPRequestHandler, HTTPServer
from src.interfaces.http.routes import handle_request


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        handle_request(self)

    def do_POST(self):
        handle_request(self)


def run_server():
    server = HTTPServer(
        ("localhost", 8000),
        RequestHandler,
    )

    print("Server running on http://localhost:8000")

    server.serve_forever()
