#we will store standard route of our website
from flask import Blueprint,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required,current_user
from .models import User,hostellite
from . import mess_db
from .models import mess
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

@views.route('/add_hostellite')
def add_hostellite():
    return render_template('add_hostellite.html')

@views.route('/add_mess')
def add_mess():
    return render_template('add_mess.html')


@views.route('/warden_dahsboard')
def warden_dashboard():
    return render_template('warden_dashboard.html')

@views.route('/roomsandservices/<username>/<hostel>')
def roomands(username,hostel):
    order = mess.query.order_by(mess.day).all()
    return render_template('RoomandServices.html',username=username,orders= order,hostel=hostel)

@views.route('/rent/<username>/<hostel>')
def rent(username,hostel):
    order = mess.query.order_by(mess.day).all() 
    return render_template('hhpaymentform.html',username=username,orders= order,hostel=hostel)

@views.route('/messageforwardem')
def message_for_warden():
    return render_template('message_for_warden.html')

@views.route('/search_hostellite/<name_user>/<hostel>')
def search(name_user,hostel):
    order = mess.query.order_by(mess.day).all() 
    return render_template('search.html',info=None,more_info = None,name_user=name_user,orders= order,hostel=hostel)

@views.route('/hostellite_dashboard/<username>/<hostel>')
def hostellite_dashboard(username,hostel):
    order = mess.query.order_by(mess.day).all() 
    return render_template('dashboard_hostellite.html',username=username,orders= order,hostel=hostel)