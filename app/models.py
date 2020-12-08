from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)

class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
