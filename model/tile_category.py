from mongoengine import *


class tile_category(Document):
    name=StringField(required=True)