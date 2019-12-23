from flask import *

privacy_policy_view = Blueprint('privacy_policy_view', __name__)


@privacy_policy_view.route("/privacy_policy")
def index():
    return render_template('pages/privacy_policy/index.html')