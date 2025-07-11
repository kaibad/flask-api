from flask import jsonify, request

from app import app
from model.user_model import UserModel

obj = UserModel()


@app.route("/user/getall", methods=["GET"])
def user_getall_controller():
    result = obj.user_getall_model()
    return jsonify(result)


@app.route("/user/signup", methods=["POST"])
def user_signup_controller():
    result = obj.user_signup_model(request.form)
    return jsonify(result)


@app.route("/user/updateprofile", methods=["PUT"])
def user_update_profile():
    result = obj.user_updateprofile_model(request.form)
    return jsonify(result)
