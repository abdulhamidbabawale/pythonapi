from flask import Flask ,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
app=Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL")
#postgresql://hamidsdata_user:BzfJkhlcTfjLxUS8tkbiQiVrwCHSI49X@dpg-cr1ohk5umphs73agmbpg-a.oregon-postgres.render.com/hamidsdata
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)


from miniapp import routes
