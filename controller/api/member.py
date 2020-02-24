from flask import Blueprint,request
from model.result import result
from model.member import member
from bson import ObjectId
from model.member_transaction import transaction
from mongoengine import NotUniqueError
from utils.auth import auth

import datetime

member_api = Blueprint('member_api', __name__)


@member_api.route('/api/member/pagination/<page>',methods=['GET'])
@auth.login_required
def get_member_data_by_page_num(page):
    page = int(page)
    items_per_page = 10
    offset = (page - 1) * items_per_page
    members = member.objects(is_active=True).skip(offset).limit(items_per_page).all()

    member_list = []

    i=0
    try:
        while i < 10:
            member_list.append(members[i])
            i += 1

    except:
        None

    pag = {
        "data": member_list,
        "total": member.objects(is_active=True).count()
    }

    res = result(True, pag, None)
    return res.convert_to_json()


@member_api.route('/api/member/search/<phone_number>',methods=['GET'])
@auth.login_required
def search_member(phone_number):
    search_result = member.objects(phone=phone_number).first()
    res = result(True,search_result,None)
    return res.convert_to_json()


@member_api.route('/api/member',methods=['POST'])
@auth.login_required
def add_member():
    try:

        form = request.form
        end_date = datetime.datetime.utcnow()+datetime.timedelta(hours=13)
        new_member = member(point=0,name=form['name'],email=form['email'],address=form['address'],phone=form['phone'],company=form['company'],is_active=True,end_date=end_date)
        new_member.save()
        res = result(True,"success",None)
        return res.convert_to_json()
    except NotUniqueError:
        res = result(False,None,'Phone Number exists.')
        return res.convert_to_json(), 400

    except:
        res = result(False, None, 'Server Error')
        return res.convert_to_json(), 500

@member_api.route('/api/member/add_point/<id>/<point>',methods=['POST'])
@auth.login_required
def add_point(id,point):
    found_member = member.objects(id=ObjectId(id)).first()

    if found_member != None:

        found_member.update(point=int(found_member['point'])+int(point)) #更新积分

        transaction(member_id=ObjectId(id),date_time=datetime.datetime.utcnow()+datetime.timedelta(hours=13),point=int(point),add_or_use=True).save()

        res = result(True, "success", None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400


@member_api.route('/api/member/use_point/<id>/<point>', methods=['POST'])
@auth.login_required
def use_point(id, point):
    found_member = member.objects(id=ObjectId(id)).first()

    if found_member != None:
        update_point=int(found_member['point']) - int(point)
        if update_point < 0:
            res = result(False, None, "积分不够")
            return res.convert_to_json(),400
        else:

            found_member.update(point=update_point)
            transaction(member_id=ObjectId(id), date_time=datetime.datetime.utcnow() + datetime.timedelta(hours=13),
                        point=int(point), add_or_use=False).save()


            res = result(True, "success", None)
            return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400

