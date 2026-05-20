from src.domain.services.auth_service import AuthService
from src.infrastructure.repositories.user_repository import UserRepository


class RegisterUserUseCase:

    def __init__(self):
        self.auth_service = AuthService()
        self.user_repository = UserRepository()

    def execute(
        self,
        email: str,
        password: str,
        role: str = "user"
    ):

        existing_user = self.user_repository.get_by_email(email)

        if existing_user:
            raise ValueError("User already exists")

        user = self.auth_service.register_user(
            email=email,
            password=password,
            role=role
        )

        return self.user_repository.create(user)
