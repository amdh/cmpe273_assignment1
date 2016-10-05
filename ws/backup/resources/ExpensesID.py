from flask import Flask, request , json, jsonify
from flask_restful import Resource, Api, reqparse, abort
from models.Expenses import Expenses, db
from flask_sqlalchemy import SQLAlchemy



class ExpensesID(Resource):
    
    def get(self,id):
        
        expense = Expenses.query.get(id)
        if  expense is None:
            return json.dumps({ 'message':'Not found'}) , 404

        return json.dumps(Expenses.serialize(expense)) , 200
        
    def put(self,id):
        if not request.json:
            abort(400)

        expense = Expenses.query.get(id)

        if  expense is None:
           return json.dumps({ 'message':'Not found'}) , 404

        if 'name' in request.json:
            expense.name = request.json.get("name","")
        if 'email' in request.json:
               expense.email = request.json.get("email","")
        if 'category' in request.json:
               expense.category = request.json.get("category","")
        if 'description' in request.json:
               expense.description = request.json.get("description","")
        if 'link' in request.json:
               expense.link = request.json.get("link","")
        if 'estimated_costs' in request.json:
               expense.estimated_costs = request.json.get("estimated_costs","")
        if 'submit_date' in request.json:
               expense.submit_date = request.json.get("submit_date","")    
        #expense = Expenses(request.json.get("name",expense.name),request.json.get('email',expense.email),
         #request.json.get("category",expense.category), request.json.get('description',expense.description), 
         #request.json.get('link',expense.link), request.json.get('estimated_costs',expense.estimated_costs),
         #request.json.get('submit_date',expense.submit_date),)
        
        db.session.commit()
        return json.dumps(Expenses.serialize(expense)), 202

   
    def delete(self,id):
        expense = Expenses.query.get(id)
        if  expense is None:
            abort(404)
        db.session.delete(expense)
        db.session.commit()
        return json.dumps({ 'status' : '204' , 'message' : 'Deleted'}), 204