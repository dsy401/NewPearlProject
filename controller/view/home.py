from flask import render_template,Blueprint
from model.staff import staff
from model.about import about
from model.brand import brand
from model.product_category import product_category
from locale import en, cn
home_view = Blueprint('home_view', __name__)


@home_view.route('/', methods=['GET'])
def index():
    staffs = staff.objects
    abouts = about.objects
    brands = brand.objects
    product_categories = product_category.objects
    return render_template('pages/Home/index.html',
                           staffs=staffs,
                           staffs_count=staffs.count(),
                           abouts=abouts,
                           abouts_count=abouts.count(),
                           brands=brands,
                           brands_count=brands.count(),
                           product_categories=product_categories,
                           product_categories_count=product_categories.count(),
                           locale=en
                           )

@home_view.route('/cn', methods=['GET'])
def index_cn():
    staffs = staff.objects
    abouts = about.objects
    brands = brand.objects
    product_categories = product_category.objects
    return render_template('pages/Home/index.html',
                           staffs=staffs,
                           staffs_count=staffs.count(),
                           abouts=abouts,
                           abouts_count=abouts.count(),
                           brands=brands,
                           brands_count=brands.count(),
                           product_categories=product_categories,
                           product_categories_count=product_categories.count(),
                           locale=cn,
                           )