from flask import Blueprint,jsonify,request
from model.result import result
from model.user import user
from utils.auth import auth
from bson import ObjectId
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
        if found_user['password'] == form['password']:
            token = user.objects().first().generate_auth_token()
            data = {
                'token': token.decode('ascii'),
                'user_name': found_user['staff_detail']['name']
            }
            print(data)
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

# test case
# @login_api.route('/api/resource')
# @auth.login_required
# def get_resource():
#     print(request.headers)
#     return jsonify({ 'data': 'Hello, %s!' })
#
