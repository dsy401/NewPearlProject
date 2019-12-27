from mongoengine import *


class product(Document):
    code = StringField(required=True)
    image = StringField(required=True)
    product_category_id = ObjectIdField(required=True)