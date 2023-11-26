from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

"""
This is where the database schema is created/modified.
"""

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    advertisements = db.relationship('Advertisement', back_populates='category')

class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"))
    title = db.Column(db.String(40))
    description = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    image = db.Column(db.String(255))
    categoryId = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='advertisements')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    advertisements = db.relationship("Advertisement")
