from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()

def config_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    Migrate(app, db)
    
def config_ma(app):

    ma.init_app(app)