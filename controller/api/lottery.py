from flask import Blueprint,request
from model.result import result
from model.lottery import lottery
from bson import ObjectId
from utils.auth import auth


lottery_api = Blueprint('lottery_api', __name__)


@lottery_api.route('/api/lottery',methods=['GET'])
def get_all_products():
    lotterys = lottery.objects()
    lottery_list = []
    for i in range(lotterys.count()):
        lottery_list.append(lotterys[i])
    res = result(True, lottery_list, None)
    return res.convert_to_json()


@lottery_api.route('/api/lottery/<id>',methods=['DELETE'])
@auth.login_required
def delete_lottery_client(id):
    found_lottery = lottery.objects(id=ObjectId(id)).first()
    if found_lottery != None:
        found_lottery.delete()
        all_lottery = lottery.objects()
        lottery_list=[]
        for i in range(all_lottery.count()):
            lottery_list.append(all_lottery[i])
        res = result(True, lottery_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400


@lottery_api.route('/api/lottery',methods=['POST'])
@auth.login_required
def add_lottery_client():
    form = request.form
    if form['gender'] == "0":
        gender = "male"
    else:
        gender = "female"

    new_lottery = lottery(name=form['name'], phone=form['phone'], gender=gender)
    new_lottery.save()

    all_lottery = lottery.objects()
    lottery_list = []
    for i in range(all_lottery.count()):
        lottery_list.append(all_lottery[i])
    res = result(True, lottery_list, None)
    return res.convert_to_json()

@lottery_api.route('/api/lottery/<id>',methods=['PUT'])
def update_lottery_client(id):
    found_lottery = lottery.objects(id=ObjectId(id)).first()
    if found_lottery != None:
        form = request.form
        print(form['gender'])
        if form['gender'] == "0":
            gender = "male"
        else:
            gender = "female"
        found_lottery.gender = gender
        found_lottery.name = form['name']
        found_lottery.phone = form['phone']
        found_lottery.update(name=form['name'],phone = form['phone'],gender = gender)



        all_lottery = lottery.objects()
        lottery_list = []
        for i in range(all_lottery.count()):
            lottery_list.append(all_lottery[i])
        res = result(True, lottery_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400