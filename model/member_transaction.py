from mongoengine import *


class transaction(Document):
    member_id = ObjectIdField(required=True)
    date_time = DateTimeField(required=True)
    amount = DecimalField(required=True)
    pay_amount = DecimalField(required=True)
    used_point = IntField(required=True)
    before_point = IntField(required=True)
    after_point=IntField(required=True)