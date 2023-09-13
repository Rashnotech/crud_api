""" a module that handle the routing of the api """
from models import app, request, jsonify, db
from models.User import User


@app.route('/api', methods=['POST', 'GET'])
@app.route('/api/create', methods=['POST'])
def create():
    """ a function that handles create function"""
    if request.method == 'GET':
        return jsonify({})
    
    if request.method == 'POST':
        name = request.form['name']
        user = User(name)
        db.session.add(user)
        db.session.commit()

        return (jsonify({}))

@app.route('/api/<int:id>')
def read(id):
    """ a function that read user details from db """
    user = User.query.filter_by(user_id=id).first()
    if user:
        return jsonify({})
    return jsonify({})

@app.route('/api/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    """ a function that update user details in db """
    user = User.query.filter_by(user_id=id)
    if request.method == 'POST':
        if user:
            db.session.delete(user)
            db.session.commit()
            name = request.form['name']
            user = User(name=name)

            db.session.add(user)
            db.session.commit()
            return jsonify({})
        return jsonify({})
    return jsonify({})

@app.route('/api/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    """ a function that delete details from db"""
    user = User.query.filter_by(user_id=id)
    if request.method == 'POST':
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({})
        return jsonify({})