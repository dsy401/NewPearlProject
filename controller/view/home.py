from flask import Blueprint, render_template
from model.staff import staff
from model.about import about
home_view = Blueprint('home_view', __name__)


@home_view.route('/', methods=['GET'])
def index():
    staffs = staff.objects
    abouts = about.objects
    return render_template('pages/Home/index.html',
                           staffs=staffs,
                           staffs_count=staffs.count(),
                           abouts=abouts,
                           abouts_count=abouts.count()
                           )
