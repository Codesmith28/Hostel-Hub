"""
from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError
from flask_bcrypt import Bcrypt 
import os

app = Flask(__name__)
db_name = "database.db"
basedir = os.path.abspath(os.path.dirname('CSE_PROJ\database.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
# Initialize The Database
app.config['SECRET_KEY'] = 'hostel_manage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(15),nullable=False)
    password = db.Column(db.String(30),nullable=False)
    hostel = db.Column(db.String(50),nullable=False)

@app.route('/')
def index():
    return render_template('profiles.html')

@app.route('/redtologin')
def redtologin():
        return render_template("login.html")


@app.route('/redtowardenlogin')
def redtowardenlogin():
    return render_template('warden_login.html')

@app.route('/redtowardenregister')
def redtowardenregister():
    return render_template('warden_register.html')

@app.route('/register',methods=['GET','POST'])
def register():
    data = request.form
    print(data)
    return render_template("warden_register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    db.session.add(data)
    db.commit()
    return render_template("warden_login.html")
if(__name__ == '__main__'):
    app.run(debug=True)
"""
from hostel import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    