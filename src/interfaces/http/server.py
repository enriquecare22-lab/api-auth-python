from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        self.wfile.write(b"Auth API Running")


def run_server():
    server = HTTPServer(
        ("localhost", 8000),
        RequestHandler
    )

    print("Server running on http://localhost:8000")

    server.serve_forever()
