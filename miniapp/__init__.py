from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
app=Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL")

db=SQLAlchemy(app)
ma=Marshmallow(app)


from miniapp import routes
