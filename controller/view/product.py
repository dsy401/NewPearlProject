from flask import *
from language import language
from model.product import product
from bson import ObjectId
product_view = Blueprint('product_view', __name__)


@product_view.route("/product/<id>")
def index(id):
    en = language['en']

    pipeline = [
        {
            "$match": {
                "_id": ObjectId(id)
            }
        },
        {
            "$lookup": {
                "from": "product_category",
                "localField": "product_category_id",
                "foreignField": "_id",
                "as": "product_category"
            }
        },
        {
            "$unwind": "$product_category"
        }
    ]

    found_product = list(product.objects.aggregate(*pipeline))[0]

    return render_template('pages/Product/index.html',locale=en,product=found_product)


@product_view.route("/product/cn/<id>")
def index_cn(id):
    cn = language['cn']
    pipeline = [
        {
            "$match": {
                "_id": ObjectId(id)
            }
        },
        {
            "$lookup": {
                "from": "product_category",
                "localField": "product_category_id",
                "foreignField": "_id",
                "as": "product_category"
            }
        },
        {
            "$unwind": "$product_category"
        }
    ]

    found_product = list(product.objects.aggregate(*pipeline))[0]

    return render_template('pages/Product/index.html', locale=cn, product=found_product)