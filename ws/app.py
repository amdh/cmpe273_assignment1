from flask import Flask, jsonify, abort, request, json, Response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from expenses_model import Expenses, db
from sqlalchemy import create_engine

app = Flask(__name__)



class createDB:
    
    def _init_(self):
        import SQLAlchemy
        
        engine = sqlalchemy.create_engine('mysql+pymysql://root:root/mysqlserver')
        engine.execute('create database if not exists expenses_management_system')

@app.route("/v1/expenses/<int:id>", methods=['GET'])
def getExpense(id):
    createDB()
    db.create_all()
    expense = Expenses.query.get(id)
    if  expense is None:
         return Response(status=404)

    ret_expense = {
        'id':expense.id,
        'name':expense.name,
        'email':expense.email,
        'category':expense.category,
        'description':expense.description,
        'link':expense.link,
        'estimated_costs':expense.estimated_costs,
        'submit_date':expense.submit_date,
        'status':expense.status,
        'decision_date':expense.decision_date

    }
    res = Response(json.dumps(ret_expense) , status=200)
    return res
    

@app.route("/v1/expenses", methods=['GET'])
def getExpenses():
    # print "inside get"
    expenses = list(Expenses.query.all())
    #print "data", expenses
    res = Response(json.dumps(Expenses.serialize_list(expenses)),status= 200, mimetype='application/json')
    return res

@app.route('/v1/expenses', methods=['POST'])
def createExpense():
    createDB()
    db.create_all()

    temp=request.get_json(force=True)
   
    expense = Expenses(temp['name'], temp['email'],temp['category'], temp['description'],  temp['link'],
    temp['estimated_costs'], temp['submit_date'])
    db.session.add(expense)
    db.session.commit()

    ret_expense = {
        'id':expense.id,
        'name':expense.name,
        'email':expense.email,
        'category':expense.category,
        'description':expense.description,
        'link':expense.link,
        'estimated_costs':expense.estimated_costs,
        'submit_date':expense.submit_date,
        'status':expense.status,
        'decision_date':expense.decision_date

    }
    a= json.dumps(ret_expense)
    res = Response(response=a,status= 201, mimetype='application/json')
    return res    
    

@app.route('/v1/expenses/<int:id>', methods=['PUT'])
def updateExpense(id):
  
    expense = Expenses.query.get(id)
    
    if  expense is None:
       return Response(status=404)

    ret_expense = {
        'id':expense.id,
        'name':expense.name,
        'email':expense.email,
        'category':expense.category,
        'description':expense.description,
        'link':expense.link,
        'estimated_costs':expense.estimated_costs,
        'submit_date':expense.submit_date,
        'status':expense.status,
        'decision_date':expense.decision_date

    }
    temp=request.get_json(force=True)
    for k,v in temp.items():
       ret_expense.update({k:v})  

    expense.name = ret_expense['name']
    expense.email = ret_expense['email']
    expense.category = ret_expense['category']
    expense.description = ret_expense['description']
    expense.link = ret_expense['link']
    expense.submit_date = ret_expense['submit_date']
    expense.estimated_costs = ret_expense['estimated_costs']
            
    db.session.commit()

    
    res = Response(status=202)
    return res


@app.route('/v1/expenses/<int:id>', methods=['DELETE'])
def deleteExpense(id):
    expense = Expenses.query.get(id)
    if  expense is None:
          return Response(status=404)
   
    db.session.delete(expense)
    db.session.commit()
    res = Response(status=204)
    return res
    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')