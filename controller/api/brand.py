from flask import Blueprint,request
from model.brand import brand
from model.result import result
from utils.auth import auth
from bson import ObjectId


brand_api = Blueprint('brand_api', __name__)

@brand_api.route('/api/brand',methods=["GET"])
def get_brand_data():
    brands = brand.objects()
    brand_list = []
    for i in range(brands.count()):
        brand_list.append(brands[i])
    res = result(True, brand_list, None)
    return res.convert_to_json()

@brand_api.route('/api/brand',methods=["POST"])
@auth.login_required
def post_brand_data():
    form = request.form

    new_brand = brand(name=form['name'], name_cn=form['name_cn'],description=form['description'],description_cn=form['description_cn'],image=form['image'])

    new_brand.save()

    all_brand = brand.objects()
    brand_list = []
    for i in range(all_brand.count()):
        brand_list.append(all_brand[i])
    res = result(True, brand_list, None)
    return res.convert_to_json()


@brand_api.route('/api/brand/<id>',methods=['DELETE'])
@auth.login_required
def delete_brand_data(id):
    found_brand = brand.objects(id=ObjectId(id)).first()
    if found_brand != None:
        found_brand.delete()

        all_brand= brand.objects()
        brand_list = []
        for i in range(all_brand.count()):
            brand_list.append(all_brand[i])
        res = result(True, brand_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400


@brand_api.route('/api/brand/<id>',methods=['PUT'])
@auth.login_required
def update_brand_data(id):
    found_brand = brand.objects(id=ObjectId(id)).first()
    if found_brand != None:
        form = request.form
        found_brand.update(
            name=form['name'],name_cn=form['name_cn'],description=form['description'],description_cn=form['description_cn'],image=form['image']
        )

        brands = brand.objects()
        brand_list = []
        for i in range(brands.count()):
            brand_list.append(brands[i])
        res = result(True, brand_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400
