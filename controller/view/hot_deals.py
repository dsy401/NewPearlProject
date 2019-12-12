from flask import *
from data_config import *
hot_deals_views = Blueprint('hot_deals', __name__)


@hot_deals_views.route("/store/hotdeals")
def hot_deals():

    return render_template('pages/Product/hotdeals/index.html', **contact_info,**category_info,active_position="Hot Deals")
