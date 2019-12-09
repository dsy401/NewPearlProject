from flask import *
from controller.api.contact import contact_api
from controller.view.home import home_view
from flask_mongoengine import MongoEngine
from config import config

# flask app config
app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = config['db']

# API config
app.register_blueprint(contact_api)


# View config
app.register_blueprint(home_view)


# db config
db = MongoEngine(app)

if __name__ == '__main__':

    # app.run()

    from waitress import serve
    serve(app,host='localhost',port=8080)
