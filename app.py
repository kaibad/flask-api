from flask import Flask

app = Flask(__name__)
# this is creating instance of Flask class and __name__ is special variable that represent the current python module


@app.route("/")  # decorator
def home():
    return "Welcome to Home Page"


from controller import *
