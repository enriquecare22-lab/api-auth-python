from src.infrastructure.repositories.user_repository import UserRepository


class GetUsersUseCase:
    def __init__(self):
        self.user_repository = UserRepository()

    def execute(self):
        users = self.user_repository.get_all()

        return [
            {
                "id": user_id,
                "email": email,
                "role": role,
            }
            for user_id, email, role in users
        ]
