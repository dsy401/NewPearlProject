from flask import Blueprint,request,abort
from model.client import client
from model.result import result


contact_api = Blueprint('contact_api', __name__)


@contact_api.route('/api/contact',methods=['POST'])
def get_contact_form():
    form = request.form
    new_client = client(name=form['name'], phone=form['phone'], email=form['email'], message=form['message'])
    new_client.save()

    res = result(True,"Your message has been sent.",None)

    return res.convert_to_json()


