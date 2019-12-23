from flask import Blueprint,request,render_template
from model.client import client
from model.result import result
from flask_mail import *
from config import config

contact_api = Blueprint('contact_api', __name__)


@contact_api.route('/api/contact',methods=['POST'])
def get_contact_form():
    # database operation
    form = request.form
    new_client = client(name=form['name'], phone=form['phone'], email=form['email'], message=form['message'])
    new_client.save()
    res = result(True, "Your message has been sent.",None)

    # 邮箱操作
    msg = Message(subject='A client contacted you just now',
                  sender='newpearldev@gmail.com',
                  recipients=[config['email_recipient']],
                  html=render_template(
                      'common/mail_template/contact_email.html',
                      form=form
                  ))
    Mail().send(msg)
    return res.convert_to_json()


@contact_api.route('/api/contact/cn',methods=['POST'])
def get_contact_form_cn():
    # database operation
    form = request.form
    new_client = client(name=form['name'], phone=form['phone'], email=form['email'], message=form['message'])
    new_client.save()
    res = result(True, "您的表单已提交.",None)
    # 邮箱操作
    msg = Message(subject='A client contacted you just now',
                  sender='newpearldev@gmail.com',
                  recipients=[config['email_recipient']],
                  html=render_template(
                      'common/mail_template/contact_email.html',
                      form=form
                  ))
    Mail().send(msg)
    return res.convert_to_json()