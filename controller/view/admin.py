from flask import Blueprint,redirect
admin_view = Blueprint('admin_view', __name__)


@admin_view.route('/admin',methods=['GET'])
def r():
    return redirect('http://www.admin.thrivingbuilding.co.nz')
