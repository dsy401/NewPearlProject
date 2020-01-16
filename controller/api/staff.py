from flask import Blueprint,request
from model.staff import staff
from model.result import result
from utils.auth import auth
from bson import ObjectId

staff_api = Blueprint('staff_api', __name__)


@staff_api.route('/api/staff',methods=["GET"])
def get_staff_data():
    staffs = staff.objects()
    staff_list = []
    for i in range(staffs.count()):
        staff_list.append(staffs[i])
    res = result(True, staff_list, None)
    return res.convert_to_json()


@staff_api.route('/api/staff/<id>',methods=['PUT'])
@auth.login_required
def update_staff_data(id):
    found_staff = staff.objects(id=ObjectId(id)).first()
    if found_staff != None:
        form = request.form
        found_staff.update(role=form['role'], role_cn=form['role_cn'],facebook=form['facebook'],linkedin=form['linkedin'],wechat=form['wechat'],image=form['image'])

        staffs = staff.objects()
        staff_list = []
        for i in range(staffs.count()):
            staff_list.append(staffs[i])
        res = result(True, staff_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400
