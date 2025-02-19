from flask import Blueprint
from flask_restful import Api
from model.user import UserResource


blueprint = Blueprint("api", __name__, url_prefix="/api")

api = Api(blueprint, errors=Blueprint.errorhandler)

api.add_resource(UserResource, "/user")
