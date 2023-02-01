from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('profiles.html')
@app.route('/',methods=['GET','POST'])
def redtologin():
    if(request.method == 'POST'):
        try:
            return render_template("login.html")
        except:
            return 'login page wasn\'t found'
if(__name__ == '__main__'):
    app.run(debug=True)