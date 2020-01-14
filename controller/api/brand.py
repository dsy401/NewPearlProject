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

    new_brand = brand(name=form['name'], name_cn=form['name_cn'],description=form['description'],description_cn=form['description_cn'],image='/static/home/img/brands/guanzhu.png')

    new_brand.save()

    all_brand = brand.objects()
    brand_list = []
    for i in range(all_brand.count()):
        brand_list.append(all_brand[i])
    res = result(True, brand_list, None)
    return res.convert_to_json()