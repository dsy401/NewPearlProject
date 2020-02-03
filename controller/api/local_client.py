from flask import Blueprint,request
from model.local_client import local_client
from model.result import result
from utils.auth import auth
from bson import ObjectId

local_client_api = Blueprint('local_client_api', __name__)


@local_client_api.route('/api/local_client',methods=["GET"])
@auth.login_required
def get_client_data():
    clients = local_client.objects(is_active=True)
    client_list = []
    for i in range(clients.count()):
        client_list.append(clients[i])
    res = result(True, client_list, None)
    return res.convert_to_json()


@local_client_api.route('/api/local_client/<id>',methods=["DELETE"])
@auth.login_required
def delete_client_data(id):
    found_client = local_client.objects(id=ObjectId(id)).first()

    if found_client != None:
        found_client.update(is_active=False)

        all_client= local_client.objects(is_active=True)
        client_list = []
        for i in range(all_client.count()):
            client_list.append(all_client[i])
        res = result(True, client_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400

@local_client_api.route('/api/local_client/<id>',methods=["PUT"])
@auth.login_required
def update_client_data(id):
    found_client = local_client.objects(id=ObjectId(id)).first()
    if found_client != None:
        form = request.form
        found_client.update(name=form['name'], phone=form['phone'], address=form['address'],email=form['email'])

        all_clients = local_client.objects(is_active=True)
        client_list = []
        for i in range(all_clients.count()):
            client_list.append(all_clients[i])
        res = result(True, client_list, None)
        return res.convert_to_json()
    else:
        res = result(False, None, "ID Error or People Not Found")
        return res.convert_to_json(), 400

@local_client_api.route('/api/local_client',methods=["POST"])
@auth.login_required
def add_client():
    form = request.form
    new_client = local_client(name=form['name'], phone=form['phone'], address=form['address'],email=form['email'],is_active=True)
    new_client.save()

    all_client = local_client.objects(is_active=True)
    client_list = []
    for i in range(all_client.count()):
        client_list.append(all_client[i])
    res = result(True, client_list, None)
    return res.convert_to_json()