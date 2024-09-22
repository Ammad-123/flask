from flask import Blueprint, request, jsonify
from models.user import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.objects().to_json()
    return users

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(**data).save()
    return jsonify(user.to_json()), 201
