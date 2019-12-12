from flask import *
from data_config import *


store_view = Blueprint('store_view', __name__)


@store_view.route('/store')
def store():
    return render_template('pages/Product/index.html', **contact_info,**category_info,active_position="Home",)


# 重定向操作
@store_view.route('/store/home')
def store_home():
    return redirect("/store")


@store_view.route('/store/index')
def store_index():
    return redirect('/store')
# 重定向操作 end
