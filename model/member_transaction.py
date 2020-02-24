from mongoengine import *


class transaction(Document):
    member_id = ObjectIdField(required=True)
    date_time = DateTimeField(required=True)
    point = IntField(required=True)
    add_or_use = BooleanField(required=True) # True 是add ，False是use