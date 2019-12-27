from flask import *
from controller.api.contact import contact_api
from controller.view.home import home_view
from controller.view.privacy_policy import privacy_policy_view
from controller.view.term_of_use import term_of_use_view
from controller.api.product import product_api
from flask_mongoengine import MongoEngine
from flask_mail import Mail
from config import config

# flask app config
app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = config['db']
app.config.update(config['mail_settings'])

# API config
app.register_blueprint(contact_api)
app.register_blueprint(product_api)

# View config
app.register_blueprint(home_view)
app.register_blueprint(privacy_policy_view)
app.register_blueprint(term_of_use_view)

# db config
db = MongoEngine(app)

# mail config
mail = Mail(app)

if __name__ == '__main__':

    # app.run(debug=True)

    from waitress import serve
    serve(app,host='localhost',port=8080)
