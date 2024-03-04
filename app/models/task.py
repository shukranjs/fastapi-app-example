from peewee import BooleanField, CharField, ForeignKeyField, TextField

from .base import BaseModel
from .user import User


class Task(BaseModel):
    user = ForeignKeyField(User, backref="tasks")
    title = CharField()
    description = TextField()
    completed = BooleanField(default=False)
