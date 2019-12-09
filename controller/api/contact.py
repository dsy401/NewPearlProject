from flask import Blueprint,request,abort
from model.client import client



contact_api = Blueprint('contact_api', __name__)


@contact_api.route('/api/contact',methods=['POST'])
def get_contact_form():
    form = request.form
    new_client = client(name=form['name'], phone=form['phone'], email=form['email'], message=form['message'])
    new_client.save()

    return {
        "is_success": True,
        "data": "Your message has been sent.",
        "error_message": None
    }


