#we will store standard route of our website
from flask import Blueprint,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required,current_user
from .models import User,hostellite
from . import mess_db
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('profiles.html')

@views.route('/hostelliteLogin')
def hostellitelogin():
    return render_template('login.html')

@views.route('/wardenLogin')
def wardenlogin():
    return render_template('warden_login.html')

@views.route('/wardenRegister')
def wardenRegister():
    return render_template('warden_register.html')

@views.route('add_hostellite')
def add_hostellite():
    return render_template('add_hostellite.html')

@views.route('add_mess')
def add_mess():
    return render_template('add_mess.html')


@views.route('warden_dahsboard')
def warden_dashboard():
    return render_template('warden_dashboard.html')

@views.route('/roomsandservices')
def roomands():
    return render_template('RoomandServices.html')

@views.route('/rent')
def rent():
    return render_template('hhpaymentform.html')

@views.route('/messageforwardem')
def message_for_warden():
    return render_template('message_for_warden.html')

@views.route('/search_hostellite')
def search():
    return render_template('search.html')