from mongoengine import *
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired,BadSignature
from config import config
from bson import ObjectId
class user(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    staff_id = ObjectIdField(required=True)

    def generate_auth_token(self, expiration=36000):
        s = Serializer(config['token']['private_key'], expires_in=expiration)
        return s.dumps({'id': str(self.id)})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(config['token']['private_key'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        the_user = user.objects(id=ObjectId(data['id'])).first()
        return the_user