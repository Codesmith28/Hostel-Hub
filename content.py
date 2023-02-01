from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('profiles.html')

@app.route('/login')
def redtologin():
        return render_template("login.html")

@app.route('/wardenlogin')
def wardenlogin():
    return render_template('warden_login.html')

if(__name__ == '__main__'):
    app.run(debug=True)