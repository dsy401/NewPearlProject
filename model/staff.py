from mongoengine import *


class staff(Document):
    name = StringField(required=True)
    role = StringField(required=True)
    role_cn = StringField(required=True)
    facebook = StringField(required=True)
    linkedin = StringField(required=True)
    wechat = StringField(required=True)
    image = StringField(required=True)