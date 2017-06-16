from peewee import *
from datetime import datetime
db = SqliteDatabase("/home/nyawira/PycharmProjects/secure_forms/my_database.db")
class User(Model):
    names = CharField()
    email = CharField(unique=True)
    age = IntegerField()
    password = CharField()
    class Meta:
        database = db

class Product(Model):

    name = CharField()
    sat =  CharField()
    date = CharField()
    owner =IntegerField()
    date_added = DateTimeField(default=datetime.now())
    class Meta:
        database = db


#Product.drop_table()
#Product.create_table()
#Product.create(name="Books kims", sat="tyu", date="erty")
#print(Product.name)

#item = Product.get(Product.id ==1)
#print(item.date_added)
# User.drop_table()
# User.create_table()
# User.create(names="John Mark", email="john@yahoo.com", age=13, password="123456")
# john = User.get(User.id == 1)
# print(john.names)