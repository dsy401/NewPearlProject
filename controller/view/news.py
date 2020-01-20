from flask import *
from language import language
from model.news_title import news_title
news_view = Blueprint('news_view', __name__)


@news_view.route("/news")
def index():
    en = language['en']
    news_titles = news_title.objects().order_by('-created_at')
    return render_template('pages/news/index.html',
                           locale=en,
                           news_titles=news_titles,
                           news_titles_count=news_titles.count()
                           )


@news_view.route('/news/cn')
def index_en():
    cn = language['cn']
    news_titles = news_title.objects().order_by('-created_at')
    return render_template('pages/news/index.html',
                           locale=cn,
                           news_titles=news_titles,
                           news_titles_count=news_titles.count()
                           )