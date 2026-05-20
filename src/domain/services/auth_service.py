from src.core.security import hash_password
from src.domain.entities.user import User


class AuthService:

    def register_user(
        self,
        email: str,
        password: str,
        role: str = "user"
    ) -> User:

        if "@" not in email:
            raise ValueError("Invalid email")

        return User(
            id=None,
            email=email.lower().strip(),
            password=hash_password(password),
            role=role
        )
