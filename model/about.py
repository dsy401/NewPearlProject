from mongoengine import *


class about(Document):
    timeline = StringField(required=True)
    image = StringField(required=True)
    description = StringField(required=True)
    subheading=StringField(required=True)