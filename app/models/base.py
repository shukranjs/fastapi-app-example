from peewee import Model, MySQLDatabase

database = MySQLDatabase(
    "my_database", user="my_user", password="my_password", host="localhost", port=3306
)


class BaseModel(Model):
    class Meta:
        database = database
