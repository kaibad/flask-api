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


# request.form catches the data send form the body form but the data send from teh url is catched as


@app.route("/user/deleteprofile/<id>", methods=["DELETE"])
def user_delete_controller(id):
    result = obj.user_deleteprofile_model(id)
    return jsonify(result)
