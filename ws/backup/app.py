
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from resources.user import User
from resources.ExpensesList import ExpensesList
from resources.ExpensesID import ExpensesID

app = Flask(__name__)
api = Api(app)


api.add_resource(User,'/User')
api.add_resource(ExpensesList, '/v1/expenses')
api.add_resource(ExpensesID, '/v1/expenses/<id>')

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0')
