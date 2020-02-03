from flask import Blueprint,request,render_template
from model.web_client import web_client
from model.result import result
from model.local_client import local_client
from flask_mail import *
from config import config
from utils.auth import auth
from bson import ObjectId
contact_api = Blueprint('contact_api', __name__)


# 给本地客户发送邮件
@contact_api.route('/api/contact/local_client',methods=['POST'])
@auth.login_required
def send_email_to_local_client():
    clients = local_client.objects(is_active=True)
    client_email_list = []
    for i in range(clients.count()):
        client_email_list.append(clients[i]['email'])

    form = request.form
    msg = Message(
        subject=form['subject'],
        sender="info@thrivingbuilding.co.nz",
        recipients=client_email_list,
        html=render_template('common/mail_template/mail_to_client_template.html',content=form['content'])
    )

    Mail().send(msg)
    res = result(True, "Your email has been sent.", None)
    return res.convert_to_json()


@contact_api.route('/api/contact/local_client/test',methods=['POST'])
@auth.login_required
def test_email_template():
    form = request.form
    msg = Message(
        subject=form['subject'],
        sender="info@thrivingbuilding.co.nz",
        recipients=[form['target_email']],
        html=render_template('common/mail_template/mail_to_client_template.html', content=form['content'])
    )

    Mail().send(msg)
    res = result(True, "Your email has been sent.", None)
    return res.convert_to_json()


@contact_api.route('/api/contact',methods=['POST'])
def post_contact_form():
    # database operation
    form = request.form
    new_client = web_client(name=form['name'], phone=form['phone'], email=form['email'], message=form['message'])
    new_client.save()
    res = result(True, "Your message has been sent.",None)

    # 邮箱操作
    msg = Message(subject='A client contacted you just now',
                  sender='info@thrivingbuilding.co.nz',
                  recipients=[config['email_recipient']],
                  html=render_template(
                      'common/mail_template/contact_email.html',
                      form=form
                  ))
    Mail().send(msg)
    return res.convert_to_json()


@contact_api.route('/api/contact/cn',methods=['POST'])
def post_contact_form_cn():
    # database operation
    form = request.form
    new_client = web_client(name=form['name'], phone=form['phone'], email=form['email'], message=form['message'])
    new_client.save()
    res = result(True, "您的表单已提交.",None)
    # 邮箱操作
    msg = Message(subject='A client contacted you just now',
                  sender='info@thrivingbuilding.co.nz',
                  recipients=[config['email_recipient']],
                  html=render_template(
                      'common/mail_template/contact_email.html',
                      form=form
                  ))
    Mail().send(msg)
    return res.convert_to_json()


@contact_api.route('/api/contact',methods=["GET"])
@auth.login_required
def get_contact_form():
    clients = web_client.objects()
    client_list = []
    for i in range(clients.count()):
        client_list.append(clients[i])
    res = result(True, client_list, None)
    return res.convert_to_json()


@contact_api.route('/api/contact/<id>',methods=['DELETE'])
@auth.login_required
def delete_contact_form(id):
    found_client = web_client.objects(id=ObjectId(id)).first()

    if found_client != None:
        found_client.delete()
        all_client= web_client.objects()
        client_list = []
        for i in range(all_client.count()):
            client_list.append(all_client[i])
        res = result(True, client_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400