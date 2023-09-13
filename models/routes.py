""" a module that handle the routing of the api """
from models import app, request, jsonify, db
from models.User import User
from models import datetime


@app.route('/api', methods=['POST', 'GET'])
@app.route('/api/create', methods=['POST'])
def create():
    """ a function that handles create function"""
    if request.method == 'GET':
        users = User.query.all()
        user_list = [{'id': user.id, 'name': user.name} for user in users]
        return jsonify(user_list)
    
    if request.method == 'POST':
        name = request.form.get('name')
        if name and isinstance(name, str):
            new_user = User(name=name)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'User created successfully'})
        return jsonify({'error': 'Name is required'}), 400    

@app.route('/api/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(id):
    """ a function that read user details from db """
    user = User.query.get(id)

    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if request.method == 'GET':
        return jsonify({'id': user.id, 'name': user.name})
    
    if request.method == 'PUT':
        name = request.form.get('name')
        if name:
            user.name = name
            user.updated_at = datetime.utcnow
            db.session.commit()
            return jsonify({'message': 'User updated successfully'})
        return jsonify({'error': 'Name is required'}), 400
    
    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})