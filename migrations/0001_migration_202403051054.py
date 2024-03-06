# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    username = CharField(max_length=255, unique=True)
    email = CharField(max_length=255)
    class Meta:
        table_name = "user"


@snapshot.append
class Task(peewee.Model):
    user = snapshot.ForeignKeyField(backref='tasks', index=True, model='user')
    title = CharField(max_length=255)
    description = TextField()
    completed = BooleanField(default=False)
    class Meta:
        table_name = "task"


