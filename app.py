from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask-book-movie-kelompok'

@app.route('/')
def index():
    return render_template('index.html')