from flask import Flask
from flask_restful import Resource, Api

class User(Resource):
    def get(self):
        return { 'name' : 'amruta', 'major':'SE'}

    def post(self):
        return {'status':'success'}