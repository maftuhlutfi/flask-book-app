from datetime import datetime
import math
from decorators import admin_required
from app import app, db
from flask import render_template, request, jsonify
import os

@app.route('/admin')
@admin_required
def admin_dashboard():
    cols = db.books.find() 

    users_count = db.users.count_documents({})

    books = []

    for x in cols:
        books.append(x)

    genre_data = map_genres(books)
    published_date_data = map_published_date(books)
    ratings_data = map_rating(books)
    languages_data = map_languages(books)

    return render_template('dashboard.html', genre_data=genre_data, users_count=users_count, books_count=len(books), published_date_data=published_date_data, ratings_data=ratings_data, languages_data=languages_data)

@app.route('/admin/catalog')
@admin_required
def admin_catalog():
    cols = db.books.find()

    books = []

    for x in cols:
        books.append(x)
    return render_template('catalog.html', books=books)

@app.route('/admin/catalog/edit', methods=["GET", "PUT"])
@admin_required
def edit_book():
    if request.method == "GET":
        book_id = request.args.get('id')
        book = db.books.find_one({ "_id": book_id })
        return render_template('editbook.html', book=book)
    if request.method == 'PUT':
        file = request.files['image'] if request.files else None
        book_id = request.form.get('id')

        books_data = {
            "title": request.form.get('title'),
            "description": request.form.get('description'),
            "author": request.form.get('author'),
            "publisher": request.form.get('publisher'),
            "published_date": request.form.get('published_date'),
            "total_pages": int(request.form.get('total_pages')),
            "isbn": request.form.get('isbn'),
            "language": request.form.get('language'),
            "genre": request.form.get('genre'),
            "price": float(request.form.get('price')),
            "link": request.form.get('link')
        }

        list_pub_data = books_data['published_date'].split('-')
        published_date = datetime(int(list_pub_data[0]), int(list_pub_data[1]), int(list_pub_data[2]))

        if file:
            extension = file.filename.rsplit('.', 1)[1]
            file.save(os.path.join('uploads/books-image', book_id + '.' + extension))
            path = '/uploads/books-image/' + book_id + '.' + extension
            books_data = {**books_data, 'image': path}

        db.books.update_one({"_id": book_id}, {"$set": {**books_data, 'published_date': published_date, 'last_updated': datetime.now()}})
        return jsonify({"message": "Successfully edit book"})
        

@app.route('/admin/scrap')
@admin_required
def admin_scrap():
    cols = db.scrap_logs.find().sort('created', -1)

    logs = []

    for x in cols:
        logs.append(x)

    return render_template('scrap.html', logs=logs)

def map_genres(books):
    genres = []

    for book in books:
        for genre in book['genres']:
            genres.append(genre)
    
    genres_distinct = list(set(genres))
    result = []

    for genre in genres_distinct:
        o = {
            "label": genre,
            "value": genres.count(genre)
        }

        result.append(o)
    
    def sort_by_value(r):
        return r['value']

    result.sort(key=sort_by_value, reverse=True)
    return result[0:5]

def map_published_date(books):
    dates = []

    for book in books:
        dates.append(int(book['published_date'].strftime("%Y")))
    
    dates_distinct = list(set(dates))
    result = []

    for date in dates_distinct:
        o = {
            "label": date,
            "value": dates.count(date)
        }

        result.append(o)
    
    def sort_by_year(r):
        return r['label']

    result.sort(key=sort_by_year)
    return result[0:5]

def map_rating(books):
    ratings = []

    for book in books:
        ratings.append(math.floor(book['rating']))
    
    ratings_distinct = [0, 1, 2, 3, 4]
    result = []

    for rating in ratings_distinct:
        o = {
            "label": rating,
            "value": ratings.count(rating)
        }

        result.append(o)
    
    def sort_by_rating(r):
        return r['label']

    result.sort(key=sort_by_rating)
    return result

def map_languages(books):
    languages = []

    for book in books:
        languages.append(book['language'] if book['language'] == 'Indonesian' or book['language'] == 'English' else 'Other')
    
    languages_distinct = list(set(languages))
    result = []

    for language in languages_distinct:
        print(language, languages.count(language))
        o = {
            "label": language,
            "value": languages.count(language)
        }

        result.append(o)
    
    def sort_by_value(r):
        return r['value']

    result.sort(key=sort_by_value)
    return result