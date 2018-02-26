from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/users/<string:username>')
def hello_world(username=None):
    return("Hello {}!".format(username))
