from dataclasses import dataclass


@dataclass
class User:
    id: str | None
    email: str
    password: str
    role: str = "user"
