from flask import *
from data_config import *
from model.product import *
from urllib import parse
from math import *
from bson import ObjectId
from model.tile_category import *
tiles_categories_view = Blueprint('tiles_categories_view', __name__)


@tiles_categories_view.route("/product/tiles_categories")
def tiles_categories():
    # categories 菜单
    tile_categories = tile_category.objects.all()
    # query-string 判断
    query = parse.parse_qs(request.query_string)

    if b'tile_category_id' in query:
        categories = query[b'tile_category_id']
    else:
        categories = []

    if b'page' in query:
        page = int(query[b'page'][0].decode('utf-8'))
    else:
        page = 1
    categories = [ObjectId(category.decode('utf-8')) for category in categories]

    if b'lowest_bound' in query and b'highest_bound' in query:
        lowest_bound = int(query[b'lowest_bound'][0].decode('utf-8'))
        highest_bound = int(query[b'highest_bound'][0].decode('utf-8'))
    else:
        lowest_bound = 0
        highest_bound = 999

    if b'tile_category_id' in query:
        pipeline = [{
            "$lookup": {
                'from': 'tile_category',
                'localField': 'tile_category_id',
                "foreignField": '_id',
                "as": "tile_category"
            },
        },
            {
                "$unwind": "$tile_category"
            },
            {
                "$match": {
                    "$or": [
                        {
                            "tile_category_id": {
                                "$in": categories
                            }
                        },
                    ],
                    "$and": [
                        {
                            "price": {
                                "$gt": lowest_bound,
                                "$lt": highest_bound
                            }
                        }
                    ]
                }
            }
        ]
    else:
        pipeline = [{
            "$lookup":{
                'from': 'tile_category',
                'localField': 'tile_category_id',
                "foreignField": '_id',
                "as": "tile_category"
            }
        },
            {
                "$unwind": "$tile_category"
            },
            {
                "$match": {
                    "$and": [
                        {
                            "price": {
                                "$gt": lowest_bound,
                                "$lt": highest_bound
                            }
                        }
                    ]
                }
            }
        ]

    products = list(product.objects.aggregate(*pipeline))
    total_page_num = floor(len(products)/15+1)
    products_to_show = products[(page-1)*15:page*15]

    return render_template('pages/Product/tiles_categories/index.html',
                           **contact_info, **category_info,
                           active_position="Tiles Categories",
                           total_page_num=total_page_num+1,
                           current_page=page,
                           products_to_show=products_to_show,
                           tile_categories=tile_categories,
                           highest_bound=highest_bound,
                           lowest_bound = lowest_bound,
                           total_product_num=len(products),
                           product_to_show_len = len(products_to_show)
                           )