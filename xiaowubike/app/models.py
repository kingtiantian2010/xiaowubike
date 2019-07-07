from . import mongodb as db


# 自行车表bike
class Bike(db.Document):
    id = db.IntField(primary_key=True)
    status = db.IntField()
    latitude = db.StringField(max_length=64)
    longitude = db.StringField(max_length=64)


# 用户表user
class User(db.Document):
    id = db.IntField(primary_key=True)
    status = db.IntField()
    phoneNum = db.StringField(unique=True)
    name = db.StringField()
    idNum = db.StringField()  # 身份证号码
    deposit = db.StringField()  # 存款
    balance = db.StringField()  # 余额
