from flask import Blueprint,request
from model.result import result
from model.member import member
from bson import ObjectId
from model.member_transaction import transaction
from mongoengine import NotUniqueError
from utils.auth import auth
from decimal import *
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
        end_date = datetime.datetime.utcnow() + datetime.timedelta(days=365)
        new_member = member(point=0,member_level=0,name=form['name'],email=form['email'],address=form['address'],
                            phone=form['phone'],company=form['company'],is_active=True,end_date=end_date,total_consumption=0)
        new_member.save()
        res = result(True,"success",None)
        return res.convert_to_json()
    except NotUniqueError:
        res = result(False,None,'Phone Number exists.')
        return res.convert_to_json(), 400

    except:
        res = result(False, None, 'Server Error')
        return res.convert_to_json(), 500

@member_api.route('/api/member/spend/<id>/<amount>/<used_point>',methods=['POST'])
@auth.login_required
def spend(id,amount,used_point):
    found_member = member.objects(id=ObjectId(id)).first()

    if found_member != None:

        used_point = int(float(used_point))

        amount = Decimal(amount)

        update_total_consumption = found_member['total_consumption']+ amount - used_point

        if update_total_consumption < 18000:
            update_member_level = 0
        elif update_total_consumption < 38000:
            update_member_level = 1
        elif update_total_consumption < 68000:
            update_member_level = 2
        else:
            update_member_level = 3

        if found_member['member_level']==0:
            update_point = int(int(amount) / 100)
        elif found_member['member_level']==1:
            update_point = int((int(amount) / 100)* 1.2)
        elif found_member['member_level']==2:
            update_point = int((int(amount) / 100)* 1.3)
        else:
            update_point = int((int(amount) / 100)* 1.5)

        final_point = update_point + int(found_member['point']) - used_point

        found_member.update(point=final_point,total_consumption=update_total_consumption,member_level=update_member_level) #更新积分

        transaction(member_id=ObjectId(id),date_time=datetime.datetime.utcnow(),
                    amount=amount,pay_amount= amount - used_point,used_point=used_point,before_point=found_member['point'],after_point=final_point
                    ).save()

        res = result(True, "success", None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400



@member_api.route('/api/member/<id>',methods=['PUT'])
@auth.login_required
def edit_member(id):
    form = request.form
    found_member = member.objects(id=ObjectId(id)).first()

    if found_member != None:
        try:
            found_member.update(name=form['name'],email=form['email'],address=form['address'],phone=form['phone'],company=form['company'])
            res = result(True, "success", None)
            return res.convert_to_json()
        except NotUniqueError:
            res = result(False, None, 'Phone Number exists.')
            return res.convert_to_json(), 400
        except:
            res = result(False, None, 'Server Error')
            return res.convert_to_json(), 500

    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400


@member_api.route('/api/member/<id>',methods=['DELETE'])
@auth.login_required
def delete_member(id):
    found_member = member.objects(id=ObjectId(id)).first()
    if found_member != None:
        found_member.update(is_active=False)
        res = result(True, "success", None)
        return res.convert_to_json()

    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400