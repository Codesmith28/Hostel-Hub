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

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hostel_manage'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME_H}'
    hostellite_db.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME_M}'
    mess_db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,hostellite
    with app.app_context():
        db.create_all()
        hostellite_db.create_all()
        mess_db.create_all()
    return app