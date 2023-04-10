#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

#from app.extensions.databased import db


#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

#db = SQLAlchemy()
#migrate = Migrate(app, db)

#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  name = db.Column(db.String(128))


#class CRUDMixin():

  #def save(self):
    #db.session.add(self)
   # db.session.commit()
   # return self
