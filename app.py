from flask import Flask, render_template, jsonify

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['SECRET_KEY'] = 'flask-book-movie-kelompok'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/<string:book_id>')
def book(book_id):
    return render_template('book.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/scrap')
def scrap():
    return render_template('scrap.html')

@app.route('/test')
def test():
    return jsonify({
        'message': 'asdasd'
    })