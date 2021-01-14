from src import app


@app.route('/')
def index():
    return 'hi!'


@app.route('/register')
def register():
    ...