from . import db
from . import hostellite_db
from . import mess_db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(40))
    hostel = db.Column(db.String(60))


class hostellite(hostellite_db.Model, UserMixin):
    id = hostellite_db.Column(db.Integer,primary_key = True)
    username = hostellite_db.Column(db.String(50))
    hostel = hostellite_db.Column(db.String(60))
    room = hostellite_db.Column(db.String(60))
    floor = hostellite_db.Column(db.String(60))

class mess(mess_db.Model , UserMixin):
    id = mess_db.Column(mess_db.Integer,primary_key = True)
    food = mess_db.Column(mess_db.String(90))
    type = mess_db.Column(mess_db.String(60))
    day = mess_db.Column(mess_db.String(50))
    