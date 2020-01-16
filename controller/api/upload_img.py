from flask import Blueprint,request
from time import time
from google.cloud import storage
from model.result import result
from setting import private_key

upload_image_api = Blueprint('upload_image_api', __name__)

@upload_image_api.route('/api/upload_image',methods=["POST"])
def upload_image():
    files = request.files
    file = files['image']
    storage_client = storage.Client.from_service_account_json(private_key)
    bucket = storage_client.get_bucket("apt-federation-262220.appspot.com")
    blob = bucket.blob(str(int(time()))+".jpg") #文件名
    blob.upload_from_string(file.read()) #文件
    blob.make_public()

    return result(True,blob.public_url,None).convert_to_json()