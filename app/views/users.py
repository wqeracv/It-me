from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from models import User

def get():
    users = User.query.all()
    return users

def post():
    user_data = request.json
    new_user = User(
        name = user_data['name'],
        age = user_data['age'],
        gender = user_data['gender'],
        email = user_data['email']
        )
    db.session.add(new_user)
    db.session.commit()