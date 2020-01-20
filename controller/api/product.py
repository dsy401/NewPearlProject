from flask import Blueprint,request
from model.result import result
from bson import ObjectId
from model.product import product
from utils.auth import auth
product_api = Blueprint('product_api', __name__)


@product_api.route('/api/product/<product_category_id>',methods=['GET'])
def get_product_by_id(product_category_id):
    products = product.objects(product_category_id=ObjectId(product_category_id))
    products_list = []
    for i in range(products.count()):
        products_list.append(products[i])
    res = result(True,products_list,None)
    return res.convert_to_json()


@product_api.route('/api/product/search/<text>',methods=['GET'])
def get_product_by_searched_word(text):
    products = product.objects(code__contains=text)
    products_list = []
    for i in range(products.count()):
        products_list.append(products[i])
    res = result(True,products_list,None)
    return res.convert_to_json()

@product_api.route('/api/product',methods=['GET'])
def get_all_products():
    products = product.objects()
    products_list = []
    for i in range(products.count()):
        products_list.append(products[i])
    res = result(True, products_list, None)
    return res.convert_to_json()

@product_api.route('/api/product',methods=['POST'])
@auth.login_required
def add_one_product():
    form = request.form
    new_product = product(
        code=form['code'],image=form['image'],product_category_id=ObjectId(form['product_category_id']),color=form['color'],environment=form['environment'],
        finish=form['finish'],material=form['material'],price=form['price'],shape=form['shape'],size=form['size'],style=form['style'],type=form['type'],unit=form['unit'],
        color_cn=form['color_cn'],environment_cn=form['environment'],finish_cn=form['finish_cn'],material_cn=form['material_cn'],price_cn=form['price_cn'],shape_cn=form['shape_cn'],
        size_cn=form['size_cn'],style_cn=form['style_cn'],type_cn=form['type_cn'],unit_cn=form['unit_cn']
    )
    new_product.save()

    products = product.objects(product_category_id=ObjectId(form['product_category_id']))
    products_list = []
    for i in range(products.count()):
        products_list.append(products[i])
    res = result(True, products_list, None)
    return res.convert_to_json()


@product_api.route('/api/product/<id>',methods=['PUT'])
@auth.login_required
def update_one_product(id):
    found_product = product.objects(id=ObjectId(id)).first()
    if found_product != None:
        form = request.form
        found_product.update(
        code=form['code'],image=form['image'],product_category_id=ObjectId(form['product_category_id']),color=form['color'],environment=form['environment'],
        finish=form['finish'],material=form['material'],price=form['price'],shape=form['shape'],set__size__=form['size'],style=form['style'],set__type__=form['type'],unit=form['unit'],
        color_cn=form['color_cn'],environment_cn=form['environment'],finish_cn=form['finish_cn'],material_cn=form['material_cn'],price_cn=form['price_cn'],shape_cn=form['shape_cn'],
        size_cn=form['size_cn'],style_cn=form['style_cn'],type_cn=form['type_cn'],unit_cn=form['unit_cn']
        )


        products = product.objects(product_category_id=ObjectId(form['product_category_id']))
        products_list = []
        for i in range(products.count()):
            products_list.append(products[i])
        res = result(True, products_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400


@product_api.route('/api/product/<id>',methods=['DELETE'])
@auth.login_required
def delete_one_product(id):
    found_product = product.objects(id=ObjectId(id)).first()

    if found_product != None:
        product_category_id = ObjectId(found_product['product_category_id'])
        found_product.delete()

        products = product.objects(product_category_id=product_category_id)
        products_list = []
        for i in range(products.count()):
            products_list.append(products[i])
        res = result(True, products_list, None)
        return res.convert_to_json()

    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400