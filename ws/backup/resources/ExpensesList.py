from flask import Flask , jsonify, json, request
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from models.Expenses import Expenses , db
from flask_sqlalchemy import SQLAlchemy


class ExpensesList(Resource):
    
    def get(self):
       # print "inside get"
        expenses = list(Expenses.query.all())
        #print "data", expenses
        return json.dumps(Expenses.serialize_list(expenses)), 200
        

    def post(self):
        if not request.json:
            abort(400)
        expense = Expenses(request.json.get("name",""), request.json.get('email',''),request.json.get("category",""), request.json.get('description',''),  request.json.get('link',''),
        request.json.get('estimated_costs',''), request.json.get('submit_date',''),)
        db.session.add(expense)
        db.session.commit()
        parser = reqparse.RequestParser()
        args = parser.parse_args()
       
        return json.dumps(Expenses.serialize(expense)) , 201

   