from mongoengine import *


class product(Document):
    code = StringField(required=True)
    tile_category_id = StringField(required=True)
    price = DecimalField(required=True)
    image = StringField(required=True)
    previous_price = DecimalField()
    is_new = BooleanField()
    product_description_id = StringField(required=True)