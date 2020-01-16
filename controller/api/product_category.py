from flask import Blueprint,request
from model.result import result
from bson import ObjectId
from model.product_category import product_category
from utils.auth import auth
product_category_api = Blueprint('product_category_api', __name__)


@product_category_api.route('/api/product_category',methods=['GET'])
def get_product_category():
    product_categorys = product_category.objects()
    product_category_list = []
    for i in range(product_categorys.count()):
        product_category_list.append(product_categorys[i])
    res = result(True, product_category_list, None)
    return res.convert_to_json()


@product_category_api.route('/api/product_category/<id>',methods=['PUT'])
@auth.login_required
def update_product_category(id):
    found_product_category = product_category.objects(id=ObjectId(id)).first()

    if found_product_category != None:
        form = request.form
        found_product_category.update(name=form['name'],name_cn=form['name_cn'],description=form['description'],description_cn=form['description_cn'],image=form['image'])

        product_categories = product_category.objects()
        product_category_list = []
        for i in range(product_categories.count()):
            product_category_list.append(product_categories[i])
        res = result(True, product_category_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400

@product_category_api.route('/api/product_category/<id>',methods=['GET'])
def first_product_category(id):
    found_product_category = product_category.objects(id=ObjectId(id)).first()
    return result(True,found_product_category,None).convert_to_json()