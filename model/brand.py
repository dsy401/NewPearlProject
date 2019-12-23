from mongoengine import *


class brand(Document):
    name=StringField(required=True)
    name_cn = StringField(required=True)
    description = StringField(required=True)
    description_cn = StringField(required=True)
    image = StringField(required=True)