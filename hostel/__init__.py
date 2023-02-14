from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


#default database for warden
db = SQLAlchemy()
DB_NAME = "database.db"

#database for hostellite

hostellite_db = SQLAlchemy()
DB_NAME_H = "hostellite.db"

mess_db = SQLAlchemy()
DB_NAME_M = "mess.db"

message_db = SQLAlchemy()
MESSAGE_DB = "message.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hostel_manage'

    app.config['SQLALCHEMY_BINDS'] = {
        "warden_db": f'sqlite:///{DB_NAME}',
        "hostellite_db": f'sqlite:///{DB_NAME_H}',
        "mess_db": f'sqlite:///{DB_NAME_M}',
        "message_db": f'sqlite:///{MESSAGE_DB}'
    }

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostellite.db'
    hostellite_db.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mess.db'
    mess_db.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///message.db'
    message_db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,hostellite,message
    with app.app_context():
        db.create_all()
        hostellite_db.create_all()
        mess_db.create_all()
        message_db.create_all()
    return app
