from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_refresh_token_required,
    jwt_required,
    get_jwt_identity,
    create_access_token
)
from . import user, auth

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }
