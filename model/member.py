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