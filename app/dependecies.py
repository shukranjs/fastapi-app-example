from app.database import database


def get_database():
    try:
        database.connect()
        yield database
    finally:
        database.close()
