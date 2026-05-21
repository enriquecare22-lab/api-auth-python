from src.infrastructure.repositories.user_repository import UserRepository


class GetProfileUseCase:
    def __init__(self):
        self.user_repository = UserRepository()

    def execute(self, user_id: str):

        user = self.user_repository.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        return {
            "id": user[0],
            "email": user[1],
            "role": user[2],
        }
