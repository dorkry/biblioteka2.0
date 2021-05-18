from app import app, models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
engine = create_engine('sqlite:///test.db')
Base = declarative_base()
Base.metadata.create_all(engine)
#conn = sqlite3.connect('library.db')
#conn.row_factory = sqlite3.Row
#c = conn.cursor()
#c.execute("UPDATE Book SET author = 1 WHERE id = 1 OR id = 2)
#conn.commit()
#c.close()

rm = models.Author('Remi', 'Mrozik')
ks = Book('ekstremista')
