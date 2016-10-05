from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)

class ExpenseManagement(Resource):
    
    def get(self):
        expenses = Expenses.query.all()
        return { 'name' : 'amruta', 'status':'pending'}

    def post(self):
        return {'status':'approved'}

   