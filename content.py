from flask import send_from_directory
from hostel import create_app
import os

app = create_app()
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)