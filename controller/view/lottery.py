from flask import *

lottery_view = Blueprint('lottery_view', __name__)


@lottery_view.route("/lottery")
def index():
    return render_template('pages/Lottery/index.html')