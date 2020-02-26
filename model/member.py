from mongoengine import *


class member(Document):
    point = IntField(required=True)
    name = StringField(required=True)
    email = StringField(required=True)
    end_date=DateTimeField(required=True)
    address=StringField(required=True)
    phone=StringField(required=True)
    company=StringField(required=True)
    is_active=BooleanField(required=True)
    member_level = IntField(required=True)  # 0 是体验会员 1是银卡 2是金卡 3是钻石
    total_consumption= DecimalField(required=True)