from src.core.database import get_connection
from src.domain.entities.user import User


class UserRepository:

    def create(self, user: User):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (email, password, role)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (user.email, user.password, user.role)
        )

        user.id = cursor.fetchone()[0]

        conn.commit()

        cursor.close()
        conn.close()

        return user

    def get_by_email(self, email: str):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, email, password, role
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            return User(
                id=row[0],
                email=row[1],
                password=row[2],
                role=row[3]
            )

        return None
