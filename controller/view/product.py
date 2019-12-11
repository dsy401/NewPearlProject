from flask import *
from data_config import *


product_view = Blueprint('product_view', __name__)


@product_view.route('/product')
def product():
    return render_template('pages/Product/index.html', **contact_info,**category_info,active_position="Home",)


# 重定向操作
@product_view.route('/product/home')
def product_home():
    return redirect("/product")


@product_view.route('/product/index')
def product_index():
    return redirect('/product')
# 重定向操作 end
