from mongoengine import *


class about(Document):
    timeline = StringField(required=True)
    image = StringField(required=True)
    description = StringField(required=True)
    subheading=StringField(required=True)
    description_cn = StringField(required=True)
    subheading_cn = StringField(required=True)
    timeline_cn = StringField(required=True)