from flask_httpauth import HTTPBasicAuth
from flask import g
from model.user import user
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token,password):
    the_user = user.verify_auth_token(username_or_token)
    if not the_user:
        return False
    else:
        g.user = the_user
        return True