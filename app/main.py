from datetime import datetime
import os, sys
# flask
from flask import Flask, flash, render_template, jsonify, request, redirect, url_for, send_file, send_from_directory
from werkzeug.utils import secure_filename
# live reloading
from livereload import Server
# redirect
import webbrowser

UPLOAD_FOLDER = "uploads/"
DOWNLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = set(['txt', 'log', 'json', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = "elephants in the bucket"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[-1] in ALLOWED_EXTENSIONS

def serve():
    app.debug = True
    # app.run(port=8000)
    server = Server(app.wsgi_app)
    server.serve(port=8000, host='localhost', open_url=True, debug=True)

@app.route('/api/<payload>', methods=['GET', 'POST'])
def catch(payload):
    print request
    if request.method == "POST":
        content = request.get_json(silent=True)
        print "Received post with content %s" % content
        webbrowser.open_new_tab("http://docs.python.org/")
        return jsonify(content) if content else "None"
    else:
        return redirect(url_for('catch_all', path = payload))

@app.route('/')
def hello():
    now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    return render_template("index.html", timestamp = now)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path

#  curl -X POST -d '{"fizz": "buzz", "foo": "bar"}' http://github.zzz.ultrahook.com -H "Content-Type: application/json"

if __name__ == '__main__':
    serve()