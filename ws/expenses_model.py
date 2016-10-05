from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Serializer import Serializer
import datetime as dt 
from time import strftime
from sqlalchemy.dialects.mysql import VARCHAR, TEXT

from Serializer import Serializer

app = Flask(__name__)
db = SQLAlchemy(app)

class Expenses(db.Model, Serializer):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30))
    category = db.Column(db.VARCHAR(50))
    description = db.Column(db.VARCHAR(100))
    link = db.Column(db.VARCHAR(200))
    estimated_costs = db.Column(db.VARCHAR(20))
    submit_date = db.Column(db.Date, default=dt.datetime.utcnow, nullable=False)
    status = db.Column(db.String(20))
    decision_date = db.Column(db.Date)
        
    def __init__(self, name, email, category, description, link, estimated_costs, submit_date):
        self.name = name;
        self.email = email
        self.category = category
        self.description = description
        self.link = link
        self.estimated_costs = estimated_costs
        if isinstance(submit_date, basestring):
            self.submit_date = dt.datetime.strptime(submit_date, "%m-%d-%Y") #dt.datetime.today() .strftime("%m-%d-%Y")
        else:
            self.submit_date = submit_date
        self.status = "Pending"
        
    #def __repr__(self):
       # return '{%r}-{%r}-{%r}-{%r}-{%r}-{%r}-{%r}-{%r}-{%r}-{%r}',self.id,self.name,self.email,self.category,self.description,self.link,self.estimated_costs,self.status,self.decision_date
    
    def serialize(self):
        ser_obj = Serializer.serialize(self)
        
        return ser_obj

   
        
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@db/expenses_management_system"
#db.create_all()
