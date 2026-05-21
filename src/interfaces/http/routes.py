import json

from src.application.use_cases.register_user import RegisterUserUseCase
from src.application.use_cases.login_user import LoginUserUseCase
from src.application.use_cases.get_users import GetUsersUseCase

from src.core.security import decode_access_token


def handle_request(handler):

    # REGISTER
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

    # LOGIN
    elif handler.path == "/login" and handler.command == "POST":
        print(handler.path)
        print(handler.command)

        content_length = int(handler.headers["Content-Length"])
        print(content_length)

        body = handler.rfile.read(content_length)
        print(body)

        data = json.loads(body)
        print(data)

        email = data.get("email")
        password = data.get("password")

        try:

            login_user = LoginUserUseCase()

            result = login_user.execute(email=email, password=password)

            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps(result).encode())

        except Exception as e:

            handler.send_response(401)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps({"error": str(e)}).encode())

    # =====================================
    # ADMIN USERS
    # =====================================

    elif handler.path == "/users" and handler.command == "GET":

        try:

            auth_header = handler.headers.get("Authorization")

            if not auth_header:
                raise ValueError("Missing token")

            token = auth_header.split(" ")[1]

            payload = decode_access_token(token)

            if payload["role"] != "admin":
                raise ValueError("Access denied")

            get_users = GetUsersUseCase()

            users = get_users.execute()

            handler.send_response(200)

            handler.send_header("Content-Type", "application/json")

            handler.end_headers()

            handler.wfile.write(json.dumps(users).encode())

        except Exception as e:

            handler.send_response(403)

            handler.send_header("Content-Type", "application/json")

            handler.end_headers()

            handler.wfile.write(json.dumps({"error": str(e)}).encode())

    else:

        handler.send_response(404)

        handler.end_headers()

        handler.wfile.write(b"Route not found")
