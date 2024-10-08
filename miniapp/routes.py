from miniapp import app,ma,db
from flask import render_template,jsonify,request,make_response
from miniapp.models import Data

class DataSchema(ma.Schema):
     class Meta:
        fields=('id','name')

#init schema
data_schema = DataSchema()
datas_schema = DataSchema(many=True)


#status code errors
@app.errorhandler(404)
def hangle_404_error(_error):
    """return a 404 status code"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def hangle_500_error(_error):
    """return a 500 status code"""
    return make_response(jsonify({'error': 'Internal server error occured'}), 500)
@app.errorhandler(401)
def hangle_401_error(_error):
    """return a 401 status code"""
    return make_response(jsonify({'error': 'Unauthorized'}), 401)


#post data
@app.route('/api/data', methods=['POST'])
def api_post():
     name=request.json['name']

     new_data=Data(name)
     db.session.add(new_data)
     db.session.commit()

     return data_schema.jsonify(new_data),201

#get all data
@app.route('/api/data',methods=['GET'])
def get_datas():
     all_data=Data.query.all()
     result=datas_schema.dump(all_data)
     return jsonify(result)

#get data with id
@app.route('/api/data/<id>',methods=['GET'])
def get_data(id):
     data=Data.query.get(id)
     return data_schema.jsonify(data)

#update data
@app.route('/api/data/<id>',methods=['PUT'])
def update_data(id):
    data=Data.query.get(id)
    name=request.json['name']
    data.name=name
    db.session.commit()
    return data_schema.jsonify(data)
 #delete data
@app.route('/api/data/<id>',methods=['DELETE'])
def delete_data(id):
     data=Data.query.get(id)
     db.session.delete(data)
     db.session.commit()
     return data_schema.jsonify(data),200
