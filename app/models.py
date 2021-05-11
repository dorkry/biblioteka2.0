# app/models.py
from app import db

class Book(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   title = db.Column(db.String(100), index = True, unique = True)
   author = db.relationship("Author", backref ="books", lazy ="dynamic")

   def __str__(self):
       return self.title

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = False)
    surname =db.Column(db.String(100), unique = False)
    books = db.relationship("Book", backref ="author", lazy ="dynamic")

    def __str__(self):
       return f'{self.name} {self.surname}'

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book = db.Column(db.String(100), unique = False)
    available = db.Column(db.Boolean)
    date_borrow = db.Column(db.Date)
    date_return = db.Column(db.Date)
    book = db.relationship("Book", backref = "borrow_info", lazy = "dynamic")

    def __str__(self):
        return f'{self.book} {self.date_borrow} {self.date_return}'