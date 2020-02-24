from flask import Blueprint,request
from bson import ObjectId
from model.result import result
from model.user import user
from model.login_log import login_log
from utils.auth import auth
from hashlib import md5
from config import config
import datetime
auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/api/login',methods=['POST'])
def login():
    form = request.form
    pipeline = [
        {
            '$match':{
                "username": form['username']
            }
        },
        {
            '$lookup': {
                "from": "staff",
                "localField": "staff_id",
                "foreignField": "_id",
                "as": "staff_detail"
            }
        },
        {
            "$unwind": "$staff_detail"
        }
    ]
    found_user_list = list(user.objects.aggregate(*pipeline))
    found_user = found_user_list[0] if len(found_user_list) != 0 else None
    if not found_user:
        res = result(False, None, "User Not Found")
        return res.convert_to_json(), 404
    else:
        hash = md5(config['password']['private_key'].encode("utf-8"))
        hash.update(form['password'].encode('utf-8'))
        password = hash.hexdigest()
        if found_user['password'] == password:
            token = user.objects().first().generate_auth_token()
            data = {
                'token': token.decode('ascii'),
                'user_name': found_user['staff_detail']['name'],
                'user_id': str(found_user['_id'])
            }

            login_log(user_name=data['user_name'],user_id=data['user_id'],date_time=datetime.datetime.utcnow()+datetime.timedelta(hours=13)).save()

            res = result(True,data,None)
            return res.convert_to_json()
        else:
            res = result(False, None, "Password Incorrect")
            return res.convert_to_json(), 403


@auth_api.route('/api/token_validate',methods=['GET'])
@auth.login_required
def token_validate():
    return result(True,'1',None).convert_to_json()
    # 1 means valid 0 mean invalid


@auth_api.route('/api/change_password/<user_id>',methods=['POST'])
@auth.login_required
def change_password(user_id):
    form = request.form
    old_password = form['old_password']
    new_password = form['new_password']
    found_user = user.objects(id=ObjectId(user_id)).first()

    old_password_hash = md5(config['password']['private_key'].encode("utf-8"))
    old_password_hash.update(old_password.encode('utf-8'))
    if old_password_hash.hexdigest() != found_user['password']:
        return result(False,None,"The old password is incorrect.").convert_to_json(),400

    new_password_hash = md5(config['password']['private_key'].encode("utf-8"))
    new_password_hash.update(new_password.encode('utf-8'))
    found_user.update(password=new_password_hash.hexdigest())
    return result(True,"Password changed",None).convert_to_json()
