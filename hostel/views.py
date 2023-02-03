#we will store standard route of our website
from flask import Blueprint,render_template

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

@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    