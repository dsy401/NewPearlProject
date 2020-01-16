from flask import Blueprint,request
from model.result import result
from utils.auth import auth



general_api = Blueprint('general_api', __name__)


@general_api.route('/api/general/change_header_img',methods=['PUT'])
def change_header_img():
    return