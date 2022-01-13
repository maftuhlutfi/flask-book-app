from flask import Flask, render_template, jsonify, session, redirect
from functools import wraps
import pymongo
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask-book-movie-kelompok'

# Database
client = pymongo.MongoClient('mongodb+srv://user1:user1@cluster0.0qikc.gcp.mongodb.net/bookApp?retryWrites=true&w=majority')
db = client.book_app

# Decorator
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session and 'is_admin' in session['user'].keys():
            if session['user']['is_admin']:
                return f(*args, **kwargs)
            else:
                return redirect('/')
        else:
            return redirect('/')
    
    return wrap

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect('/')
        else:
            return f(*args, **kwargs)
    
    return wrap

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
@is_logged_in
def login_page():
    return render_template('login.html')

@app.route('/signup')
@is_logged_in
def register():
    return render_template('signup.html')

@app.route('/<string:book_id>')
def book(book_id):
    return render_template('book.html')

@app.route('/admin')
@admin_required
def dashboard():
    return render_template('dashboard.html', post=json.dumps(['a']))

@app.route('/admin/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/admin/scrap')
def scrap():
    return render_template('scrap.html')

@app.route('/test')
def test():
    return jsonify({
        'message': 'asdasd'
    })

from routes import user