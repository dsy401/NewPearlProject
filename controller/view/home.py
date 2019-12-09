from flask import Blueprint, render_template
home_view = Blueprint('home_view', __name__)


@home_view.route('/', methods=['GET'])
def index():
    return render_template('pages/Home/index.html')
