from flask import Blueprint,request
from model.result import result
from bson import ObjectId
from model.news_title import news_title
from model.news_content import news_content
from utils.auth import auth
from datetime import datetime
news_api = Blueprint('news_api', __name__)


@news_api.route('/api/news',methods=['POST'])
@auth.login_required
def news_publish():
    form = request.form

    new_news_title = news_title(title=form['title'],title_cn=form['title_cn'],image=form['image'],created_at=datetime.now())
    new_news_title.save()

    new_news_content = news_content(content=form['content'],content_cn=form['content_cn'],news_title_id=ObjectId(new_news_title.id))
    new_news_content.save()

    res = result(True, "Publish successfully", None)
    return res.convert_to_json()


@news_api.route('/api/news',methods=['GET'])
def get_news():
    news_titles = news_title.objects().order_by('-created_at')
    news_titles_list = []
    for i in range(news_titles.count()):
        news_titles_list.append(news_titles[i])
    res = result(True,news_titles_list,None)

    return res.convert_to_json()


@news_api.route('/api/news/<news_title_id>',methods=['DELETE'])
@auth.login_required
def delete_news(news_title_id):
    news_title.objects(id=ObjectId(news_title_id)).first().delete()
    news_content.objects(news_title_id=ObjectId(news_title_id)).first().delete()

    news_titles = news_title.objects().order_by('-created_at')
    news_titles_list = []
    for i in range(news_titles.count()):
        news_titles_list.append(news_titles[i])
    res = result(True, news_titles_list, None)
    return res.convert_to_json()


@news_api.route('/api/news/<news_title_id>',methods=['GET'])
def get_news_by_news_title_id(news_title_id):
    pipeline = [
        {
            "$match": {
                "news_title_id": ObjectId(news_title_id)
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
    found_news_content['_id'] = str(found_news_content['_id'])
    found_news_content['news_title_id'] = str(found_news_content['news_title_id'])
    found_news_content['news_title']['_id'] = str(found_news_content['news_title']['_id'])

    res = result(True,found_news_content,None)
    return res.convert_to_json()


@news_api.route('/api/news',methods=['PUT'])
@auth.login_required
def update_news():

    form = request.form
    found_news_title = news_title.objects(id=ObjectId(form['news_title_id'])).first()
    found_news_title.update(title=form['title'],title_cn=form['title_cn'],image=form['image'])

    found_news_content = news_content.objects(id=ObjectId(form['news_content_id'])).first()
    found_news_content.update(content=form['content'],content_cn=form['content_cn'])

    res = result(True, "Edit successfully", None)
    return res.convert_to_json()