import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.quote import Quote_By_Id, Quotes, Random_Quote
from resources.user import User_Login, User_Register
from db import db

app = Flask('__main__')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DB_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = os.environ.get(
    'APP_SECRET', 'Super Secure Secret!@_@')

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        "description": "The token has expired.",
        "error": "token_expired"
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        "description": "Signature verification failed.",
        "error": "invalid_token"
    }), 401


@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        "error": "authorization_required"
    }), 401


@jwt.needs_fresh_token_loader
def fresh_token_callback():
    return jsonify({
        "description": "The token is not fresh.",
        "error": "fresh_token_required"
    }), 401


api.add_resource(Quotes, "/quotes")
api.add_resource(Quote_By_Id, "/quote/<string:quote_id>")
api.add_resource(Random_Quote, "/quote/random")

api.add_resource(User_Login, "/login")
api.add_resource(User_Register, "/register")

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
