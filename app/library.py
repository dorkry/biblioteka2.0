from app import app, models, db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
#engine = create_engine('sqlite:///test.db')
#Base = declarative_base()
#Base.metadata.create_all(engine)
#conn = sqlite3.connect('library.db')
#conn.row_factory = sqlite3.Row
#c = conn.cursor()
#c.execute("UPDATE Book SET author = 1 WHERE id = 1 OR id = 2)
#conn.commit()
#c.close()
#from flask import Flask, render_template, request

#app = Flask(__name__)

#@app.route('/')
#def homepage():
    #rm = models.Author('Remi', 'Mrozik')
    #ks = models.Book('ekstremista')
    #print('jupi jeee')
    #return
