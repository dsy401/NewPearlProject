from flask import *
from language import language
news_view = Blueprint('news_view', __name__)


@news_view.route("/news")
def index():
    en = language['en']
    return render_template('pages/news/index.html',locale=en)


@news_view.route('/news/cn')
def index_en():
    cn = language['cn']
    return render_template('pages/news/index.html',locale=cn)