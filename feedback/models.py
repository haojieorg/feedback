from datetime import datetime
from run import db


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    mobile = db.Column(db.String)
    address = db.Column(db.String)
    text = db.Column(db.Text)
    c_time = db.Column(db.DateTime)

    departmentid = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', backref=db.backref('employees', lazy='dynamic'))

    def __init__(self, name=None, gender=None,mobile=None, address=None, text=None, c_time=None):
        self.name = name
        self.gender = gender
        self.mobile = mobile
        self.address = address
        self.text = text
        self.c_time = datetime.now()
