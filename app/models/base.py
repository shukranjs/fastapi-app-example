from peewee import Model, MySQLDatabase
from app.database import database


class BaseModel(Model):
    class Meta:
        database = database
