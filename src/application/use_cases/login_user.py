from src.core.security import verify_password, create_access_token

from src.infrastructure.repositories.user_repository import UserRepository


class LoginUserUseCase:

    def __init__(self):
        self.user_repository = UserRepository()

    def execute(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")

        is_valid_password = verify_password(
            password,
            user.password,
        )

        if not is_valid_password:
            raise ValueError("Invalid credentials")

        access_token = create_access_token(
            user_id=user.id,
            role=user.role,
        )

        return {
            "access_token": access_token,
        }
