import json

from src.application.use_cases.register_user import RegisterUserUseCase


def handle_request(handler):

    if handler.path == "/register" and handler.command == "POST":

        content_length = int(handler.headers["Content-Length"])

        body = handler.rfile.read(content_length)

        data = json.loads(body)

        email = data.get("email")
        password = data.get("password")

        try:

            register_user = RegisterUserUseCase()

            user = register_user.execute(email=email, password=password)

            response = {
                "message": "User registered successfully",
                "user": {"id": user.id, "email": user.email, "role": user.role},
            }

            handler.send_response(201)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()

            handler.wfile.write(json.dumps(response).encode())

        except Exception as e:

            handler.send_response(400)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()

            handler.wfile.write(json.dumps({"error": str(e)}).encode())

    else:

        handler.send_response(404)
        handler.end_headers()

        handler.wfile.write(b"Route not found")
