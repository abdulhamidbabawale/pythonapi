from . import db,app

class Data(db.Model):
    __TableName__ ='datadb'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(length=255), nullable=False)
    def __init__(self,name):
            self.name=name


with app.app_context():
     db.create_all()


