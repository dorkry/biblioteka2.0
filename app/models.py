# app/models.py
from app import db
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

book_author = db.Table('book_author', Base.metadata,
    db.Column('book_id', db.ForeignKey('Book.id'), primary_key = True),
    db.Column('author_id', db.ForeignKey('Author.id'), primary_key = True)
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True)
#many-to-many
    author = db.relationship('Author', backref ='books', lazy = 'dynamic', secondary = book_author)

    def __init__(self, title):
        self.id= uuid.uuid4().hex
        self.title =  title

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = False)
    surname =db.Column(db.String(100), unique = False)
#many-to-many
    books = db.relationship('Book', backref ='authors', lazy ='dynamic', secondary = book_author)

    def __init__(self, name, surname ):
        self.id= uuid.uuid4().hex
        self.name =  name
        self.surname = surname

#class Borrow(db.Model):
    #id = db.Column(db.Integer, primary_key = True)
    #book = db.Column(db.String(100), unique = False)
    #available = db.Column(db.Boolean)
    #date_borrow = db.Column(db.Date)
    #date_return = db.Column(db.Date)
    #book = db.relationship("Book", backref = "borrow_info", lazy = "dynamic")

