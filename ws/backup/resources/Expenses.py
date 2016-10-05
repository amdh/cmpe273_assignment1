from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from models.Expenses import Expenses
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/expenses_management_system"
db = SQLAlchemy(app)


class ExpensesID(Resource):
    
       
    def put(self,id):
        expense = Expenses.query.get(id)
        expense = Expenses(request.json.get("name",""), request.json.get("category",""), request.json.get('description',''), request.json.get('email',''), request.json.get('link',''),
        request.json.get('estimated_costs',''))
        db.session.add(expense)
        db.session.commit()
        return { 'status' : 'updated' , 'name' : 'amz'}

   
    def delete(self,id):
        db.session.delete(Expenses.query.get(id))
        db.session.commit()
        return { 'status' : 'deleted'}, 201