from flask import Blueprint,request
from model.result import result
from model.about import about
from bson import ObjectId
from utils.auth import auth

about_api = Blueprint('about_api', __name__)


@about_api.route('/api/about',methods=['GET'])
def get_about():
    abouts = about.objects()
    about_list = []
    for i in range(abouts.count()):
        about_list.append(abouts[i])
    res = result(True, about_list, None)
    return res.convert_to_json()


@about_api.route('/api/about',methods=['POST'])
@auth.login_required
def add_about():
    form = request.form
    new_about = about(timeline=form['timeline'],timeline_cn=form['timeline_cn'],
                      image=form['image'],description=form['description'],description_cn=form['description_cn'],
                      subheading=form['subheading'],subheading_cn=form['subheading_cn']
                      )
    new_about.save()

    abouts = about.objects()
    about_list = []
    for i in range(abouts.count()):
        about_list.append(abouts[i])
    res = result(True, about_list, None)
    return res.convert_to_json()


@about_api.route('/api/about/<id>',methods=['DELETE'])
@auth.login_required
def delete_about(id):
    about.objects(id=ObjectId(id)).first().delete()

    abouts = about.objects()
    about_list = []
    for i in range(abouts.count()):
        about_list.append(abouts[i])
    res = result(True, about_list, None)
    return res.convert_to_json()


@about_api.route('/api/about/<id>', methods=['PUT'])
@auth.login_required
def update_about(id):
    form = request.form
    about.objects(id=ObjectId(id)).first().update(timeline=form['timeline'],timeline_cn=form['timeline_cn'],
                      image=form['image'],description=form['description'],description_cn=form['description_cn'],
                      subheading=form['subheading'],subheading_cn=form['subheading_cn'])

    abouts = about.objects()
    about_list = []
    for i in range(abouts.count()):
        about_list.append(abouts[i])
    res = result(True, about_list, None)
    return res.convert_to_json()