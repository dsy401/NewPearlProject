from mongoengine import *


class lottery(Document):
    name=StringField(required=True)
    phone=StringField(required=True)
    gender=StringField(required=True)