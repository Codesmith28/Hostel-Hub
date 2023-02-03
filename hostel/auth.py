from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hostel = request.form.get('hostel')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password,password):
                return render_template('dashboard.html')
            else:
                flash('Incorrect password!',category='error')
                return render_template('warden_login.html')
        else:
            flash('Username doesn\'t exist',category='error')
            return render_template('warden_login.html')

    return render_template(url_for('wardenlogin'))

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        hostel = request.form.get('hostel')

        user = User.query.filter_by(username=username).first()

        if user:
            flash('Username already exists',category='error')
            return render_template('warden_register.html')
        if len(username) < 1:
            flash("Please enter a valid username.",category='error')
        elif len(password) < 7:
            flash("Please enter a password having length more than 7",category='error')
        else:
            new_user = User(username=username,password=generate_password_hash(password ,method='sha256'),hostel=hostel)
            db.session.add(new_user)
            db.session.commit()
            redirect(url_for('views.home'))
            flash('Account created',category='error')

    return render_template("warden_register.html")

