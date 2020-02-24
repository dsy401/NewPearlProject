from flask import Blueprint,request
from model.result import result
from model.member import member
from bson import ObjectId
from model.member_transaction import transaction
from mongoengine import NotUniqueError
from utils.auth import auth

import datetime

member_transaction_api = Blueprint('member_transaction_api', __name__)


@member_transaction_api.route('/api/member_transaction/<id>',methods=['GET'])
@auth.login_required
def index(id):
    found_transaction = transaction.objects(member_id=ObjectId(id)).order_by('-date_time')
    found_transaction_list = []
    for i in range(found_transaction.count()):
        found_transaction_list.append(found_transaction[i])
    res = result(True,found_transaction_list,None)

    return res.convert_to_json()