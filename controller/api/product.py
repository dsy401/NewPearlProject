from flask import Blueprint,request,render_template
from model.result import result
from bson import ObjectId
from model.product import product
product_api = Blueprint('product_api', __name__)


@product_api.route('/api/product/<product_category_id>',methods=['GET'])
def get_contact_form(product_category_id):
    products = product.objects(product_category_id=ObjectId(product_category_id))
    products_list = []
    for i in range(products.count()):
        products_list.append(products[i])
    res = result(True,products_list,None)
    return res.convert_to_json()