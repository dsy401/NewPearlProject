from flask import *

term_of_use_view = Blueprint('term_of_use_view', __name__)


@term_of_use_view.route("/term_of_use")
def index():
    return render_template('pages/term_of_use/index.html')