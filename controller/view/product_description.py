from flask import *
from data_config import *
from bson import ObjectId
from model.product import *
import random

product_description_view = Blueprint('product_description_view', __name__)


@product_description_view.route('/store/product_description/<product_description_id>')
def index(product_description_id):
    product_description_id = ObjectId(product_description_id)

    product_pipeline = [{
        "$lookup": {
            'from': 'product_description',
            'localField': 'product_description_id',
            "foreignField": '_id',
            "as": "product_description"
        },
    },
        {
          "$lookup":{
              'from': 'tile_category',
              'localField': 'tile_category_id',
              "foreignField": '_id',
              "as": "tile_category"
          }
        },
        {
            "$unwind": "$product_description"
        },
        {
          "$unwind": "$tile_category"
        },
        {
            "$match": {
               "$or":[
                   {
                       "product_description_id": {
                           "$in": [product_description_id]
                       }
                   }
               ]
            }
        }
    ]


    description = list(product.objects.aggregate(*product_pipeline))
    if len(description)==0:
        return redirect("/store/product")


    relevant_product_pipeline = [
        {
            "$match": {
                "$or": [
                    {
                        "tile_category_id": {
                            "$in": [description[0]['tile_category_id']]
                        }
                    }
                ]
            }
        }
    ]

    total_relevant_product = list(product.objects.aggregate(*relevant_product_pipeline))
    relevant_product = []
    for i in random.sample(range(0,len(total_relevant_product)),4):
        relevant_product.append(total_relevant_product[i])



    return render_template("pages/Product/product_description/index.html",
                           **contact_info, **category_info, active_position="",
                           description=description[0]['product_description'],
                           product=description[0],
                           tile_category=description[0]['tile_category']['name'],
                           relevant_product=relevant_product
                           )