from mongoengine import *


class news_title(Document):
    title = StringField(required=True)
    image = StringField(required=True)
    title_cn = StringField(required=True)
    created_at = DateTimeField(required=True)