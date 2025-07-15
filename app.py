from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# this is creating instance of Flask class and __name__ is special variable that represent the current python module
CORS(app)
# This will allow all domains (or customize with CORS(app, resources={...}))


@app.route("/")  # decorator
def home():
    return "Welcome to Home Page"


from controller import *
