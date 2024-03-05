from peewee import MySQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()


database = MySQLDatabase(
    os.getenv("DB_DATABASE", "test"),
    user=os.getenv("DB_USER", "test"),
    password=os.getenv("DB_PASSWORD", "test"),
    # host=os.getenv("DB_HOST", 'mysql'),
    port=int(os.getenv("DB_PORT", "3306")),
)
