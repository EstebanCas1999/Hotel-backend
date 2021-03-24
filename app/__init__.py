from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

api_blueprint = Blueprint('api', __name__)
CORS(api_blueprint)
api = Api(api_blueprint, prefix='/hotel-backend/private')
public_api = Api(api_blueprint, prefix='/hotel-backend/public')
