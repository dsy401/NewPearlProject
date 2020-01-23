from mongoengine import *


class news_content(Document):
    content = StringField(required=True)
    content_cn = StringField(required=True)
    news_title_id = ObjectIdField(required=True)