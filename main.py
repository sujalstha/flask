from flask import Flask

web = Flask(__name__)


@web.route('/')
def hello_world():
    return '<h1>Hello World!<h1>'
