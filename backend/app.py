from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index page</p>"

@app.route('/hello')
def hello():
    return "<p>Hello, World! page</p>"