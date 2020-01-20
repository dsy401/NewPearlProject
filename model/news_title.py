from mongoengine import *


class news_title(Document):
    title = StringField()
    image = StringField()
    title_cn = StringField()
    created_at = DateTimeField()