""" a module that handle the routing of the api """


from models import app
from models.User import User


@app.route('/api')
def hello_world():
    """ a function that handles api calls"""
    return ('<h1>Hello world</h1>')