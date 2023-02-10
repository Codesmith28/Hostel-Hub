from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User,hostellite,mess
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user , login_required , logout_user , current_user
from . import hostellite_db
from . import mess_db

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hostel = request.form.get('hostel')

        user = User.query.filter_by(username=username).first()
        hostel_exists = User.query.filter_by(hostel=hostel).first()
        if user:
            if hostel_exists:
                if check_password_hash(user.password,password):
                    return render_template('warden_dashboard.html',username=username,hostel=hostel)
                else:
                    flash('Incorrect Password Entered',category='error')
                    return render_template('warden_login.html')
        else:
            flash("Username doesn\'t exists. Please signup to get your hostel access to our site",category='error')    
            return render_template('warden_login.html')

    return render_template('warden_login.html')


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
            flash('Account created. Now please redirect to login page to access your account ',category='error')

    return render_template("warden_register.html")

@auth.route('/add_info',methods=['GET','POST'])
def add_info():
    if request.method == 'POST':
        new_name = request.form.get('new_name')
        new_floor = request.form.get('new_floor')
        new_room = request.form.get('new_room')
        new_hostel = request.form.get('hostel_name')
        new_entry = hostellite(username=new_name,hostel=new_hostel,room=new_room,floor=new_floor)

        try:
            hostellite_db.session.add(new_entry)
            hostellite_db.session.commit()
            data = hostellite.query.order_by(hostellite.username).all()
            return render_template('add_hostellite.html', datas=data)
        except:
            flash("There was problem in accessing databse",category='error')
            return render_template('add_hostellite.html')
    
    else:
        data = hostellite.query.order_by(hostellite.username).all()
        return render_template('add_hostellite.html',datas = data)

@auth.route('/add_mess',methods=['GET','POST'])
def add_mess():
    if(request.method == 'POST'):
        food = request.form.get('food')
        tye = request.form.get('type')
        day = request.form.get('day')

        new_entry = mess(food=food,type = tye,day = day)
        order = mess.query.order_by(mess.day).all()
        try:
            mess_db.session.add(new_entry)
            mess_db.session.commit()
            return render_template('add_mess.html',orders = order)
        except:
            return render_template('add_mess.html')
    else:
        return render_template('add_mess.html',orders = order)

@auth.route('/hostellite_login',methods=['GET','POST'])
def hostellite_login():
    if request.method == 'POST':
        username_h = request.form.get('username')
        hostel_h = request.form.get('hostel')
        user_h = hostellite.query.filter_by(username=username_h).first()
        hostel_exists_h = hostellite.query.filter_by(hostel=hostel_h).first()
        if hostel_exists_h:
            if user_h:               
                order = mess.query.order_by(mess.day).all()   
                return render_template('dashboard_hostellite.html',hostel = hostel_h,username=username_h,orders= order)
            else:
                flash("Username does\'nt exists please contact your hostel authoraties to create your account",category='error')
                return render_template('login.html')
        else:
            flash("Your hostel name doesnt exists on our database",category='error')
            return render_template('login.html')
    return render_template('login.html')

