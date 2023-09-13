from models import app

@app.route('/api')
def hello_world():
    return ('<h1>Hello world</h1>')