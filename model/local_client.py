from mongoengine import *


class local_client(Document):
    name = StringField(required=True)
    phone = StringField(required=True)
    email = StringField(required=True)
    address = StringField(required=True)
    is_active = BooleanField(required=True)