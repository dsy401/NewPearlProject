from flask import *
from language import language
from model.news_title import news_title
from model.news_content import news_content
from bson import ObjectId
news_view = Blueprint('news_view', __name__)


@news_view.route("/news")
def index():
    en = language['en']
    news_titles = news_title.objects().order_by('-created_at')
    print(news_titles[0]['id'])
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

@news_view.route('/news/<id>')
def get_news_content(id):
    en = language['en']
    pipeline = [
        {
            "$match": {
                "news_title_id": ObjectId(id)
            }
        },
        {
            "$lookup":{
                "from": "news_title",
                "localField": "news_title_id",
                "foreignField": "_id",
                "as": "news_title"
            }
        },
        {
            "$unwind": "$news_title"
        }
    ]
    found_news_content = list(news_content.objects.aggregate(*pipeline))[0]

    return render_template('pages/news_content/index.html',
                           locale=en,
                           news_content=found_news_content
                           )

@news_view.route('/news/cn/<id>')
def news_content_cn(id):
    cn = language['cn']
    pipeline = [
        {
            "$match": {
                "news_title_id": ObjectId(id)
            }
        },
        {
            "$lookup": {
                "from": "news_title",
                "localField": "news_title_id",
                "foreignField": "_id",
                "as": "news_title"
            }
        },
        {
            "$unwind": "$news_title"
        }
    ]
    found_news_content = list(news_content.objects.aggregate(*pipeline))[0]
    return render_template('pages/news_content/index.html',
                           locale=cn,
                           news_content=found_news_content
                           )