from mongoengine import *


class web_client(Document):
    name = StringField(required=True)
    phone = StringField(required=True)
    email = StringField(required=True)
    message = StringField(required=True)