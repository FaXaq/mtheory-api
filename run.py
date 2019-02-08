import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from server import create_app
from server import db
from server.router import route

app = create_app(os.getenv('APP_SETTINGS'))
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# assign routes
route(api)

if __name__ == '__main__':
    app.run()