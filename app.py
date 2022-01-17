from flask import Flask, render_template, jsonify, session, redirect
import pymongo
from decorators import is_logged_in

from scraper import scrap_func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask-book-movie-kelompok'

# Database
client = pymongo.MongoClient('mongodb+srv://user1:user1@cluster0.0qikc.gcp.mongodb.net/bookApp?retryWrites=true&w=majority')
db = client.book_app

@app.route('/')
def index():
    return redirect('/books')

@app.route('/books')
def books():
    cols = db.books.find()

    books = []

    for x in cols:
        books.append(x)

    return render_template('books.html', books=books)

@app.route('/login')
@is_logged_in
def login_page():
    return render_template('login.html')

@app.route('/signup')
@is_logged_in
def register():
    return render_template('signup.html')

@app.route('/books/<string:book_id>')
def book(book_id):
    book = db.books.find_one({ "_id": book_id })

    return render_template('book.html', book=book)

@app.route('/test')
def test():
    scrap_func(['https://play.google.com/store/books/details/Fanny_Fatullah_Note_Of_Kim?id=kqFQEAAAQBAJ'])
    return jsonify({
        'message': 'asdasd'
    })

@app.route('/drop')
def drop():
    db.books.drop()
    db.scrap_logs.drop()

from routes import user
from routes import admin
from routes import scrap

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug=True,use_reloader=True)