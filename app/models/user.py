from peewee import CharField

from .base import BaseModel


class User(BaseModel):
    username = CharField(unique=True)
    email = CharField()
