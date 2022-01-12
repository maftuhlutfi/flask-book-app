from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['SECRET_KEY'] = 'flask-book-movie-kelompok'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/<string:book_id>')
def book(book_id):
    return render_template('book.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')