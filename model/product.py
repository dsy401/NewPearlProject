from mongoengine import *


class product(Document):
    code = StringField(required=True)
    image = ListField(required=True)
    product_category_id = ObjectIdField(required=True)
    size = StringField(required=True)
    color = StringField(required=True)
    price=StringField(required=True)
    shape=StringField(required=True)
    style=StringField(required=True)
    unit=StringField(required=True)
    finish=StringField(required=True)
    type=StringField(required=True)
    environment = StringField(required=True)
    material=StringField(required=True)
    size_cn = StringField(required=True)
    color_cn = StringField(required=True)
    price_cn = StringField(required=True)
    shape_cn = StringField(required=True)
    style_cn = StringField(required=True)
    unit_cn = StringField(required=True)
    finish_cn = StringField(required=True)
    type_cn = StringField(required=True)
    environment_cn = StringField(required=True)
    material_cn = StringField(required=True)