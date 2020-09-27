from flask import Flask, Blueprint
from app.restplus import api
from app.config import config_db, config_ma
from app.views.author import ns_author
from app.views.book import ns_book

app = Flask(__name__)
         
config_db(app)
config_ma(app)

blueprint = Blueprint('api', __name__)
api.init_app(blueprint)
app.register_blueprint(blueprint)

api.add_namespace(ns_author)
api.add_namespace(ns_book)

app.run()