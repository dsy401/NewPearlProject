from flask import Blueprint
from model.result import result
from bson import ObjectId
from model.product_category import product_category
product_category_api = Blueprint('product_category_api', __name__)



@product_category_api.route('/api/product_category',methods=['GET'])
def get_product_category():
    product_categorys = product_category.objects()
    product_category_list = []
    for i in range(product_categorys.count()):
        product_category_list.append(product_categorys[i])
    res = result(True, product_category_list, None)
    return res.convert_to_json()