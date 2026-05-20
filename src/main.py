from src.core.database import init_db
from src.interfaces.http.server import run_server


def main():
    init_db()
    run_server()


if __name__ == "__main__":
    main()
