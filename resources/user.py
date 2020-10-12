from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    fresh_jwt_required,
    get_jwt_identity
)

from models.user import User_Model

_parser = reqparse.RequestParser()

_parser.add_argument(
    'username',
    type=str,
    required=True,
    help="This field cannot be blank."
)
_parser.add_argument(
    'password',
    type=str,
    required=True,
    help="This field cannot be blank."
)


class User_Login(Resource):
    def post(self):
        post_data = _parser.parse_args()

        user = User_Model.get_user_by_username(post_data["username"])

        if user and check_password_hash(user.password, post_data["password"]):
            access_token = create_access_token(
                identity=user.user_id, fresh=True
            )
            return {
                "access_token": access_token,
            }, 200

        return {"message": "Invalid credentials."}, 401


class User_Register(Resource):
    @fresh_jwt_required
    def post(self):
        post_data = _parser.parse_args()

        user = User_Model.get_user_by_username(post_data["username"])

        if user:
            return {"message": "Username already exists."}, 400

        post_data["password"] = generate_password_hash(post_data["password"])
        user = User_Model(**post_data)
        user.save_to_db()
        return {
            "message": "User created.",
            "info": user.json()
        }, 201
