from mongoengine import *


class login_log(Document):
    user_name=StringField(required=True)
    user_id= ObjectIdField(required=True)
    date_time= DateTimeField(required=True)