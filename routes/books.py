from datetime import datetime
from operator import ge
from flask import Flask, render_template, jsonify, session, redirect, request
from app import app, db
from decorators import admin_required, is_logged_in

@app.route('/books')
def books():
    sort_name, sort_mode = request.args.get('sort').split(' ') if request.args.get('sort') != None else ['', 'dsc']
    genre =  request.args.get('genre').split(',') if request.args.get('genre') != None else None
    languages =  request.args.get('languages').split(',') if request.args.get('languages') != None else None
    from_date = request.args.get('from')
    until_date = request.args.get('until')

    if ('logged_in' not in session and (genre or sort_name or languages or from_date or until_date)):
        return redirect('/login?from=filter-sort')

    sort_name = 'year'
    field = 'published_date'

    if sort_name != 'date' and sort_name != '':
        field = sort_name

    query_filter = get_query_filter(genre, languages, from_date, until_date)
    
    cols = db.books.find(query_filter) 

    cols.sort(field, -1 if sort_mode == 'dsc' else 1)

    books = []

    for x in cols:
        books.append(x)

    languages = []

    for book in books:
        if book['language'] not in languages:
            languages.append(book['language'])

    return render_template('books.html', books=books, languages=languages, genres=get_genres())
    
@app.route('/books/<string:book_id>')
def book(book_id):
    if 'logged_in' not in session:
        return redirect('/login?from=filter-sort')

    book = db.books.find_one({ "_id": book_id })

    return render_template('book.html', book=book)

@app.route('/books/<string:book_id>/update-status', methods=['PATCH'])
@admin_required
def update_status(book_id):
    data = request.get_json(silent=True)
    status = data["status"]

    db.books.update_one({"_id": book_id}, {"$set": {"enabled": status}})

    return jsonify({"message": ("Enabled" if status else "Disabled") + " book with id " + book_id})

@app.route('/books/<string:book_id>/delete', methods=["delete"])
def delete_book(book_id):
    db.books.delete_one({ "_id": book_id })

    return jsonify({
        'message': 'Successfully delete book with id' + book_id
    })

@app.route('/books/search')
def search_books():
    query =  request.args.get('query') if request.args.get('query') != None else None

    cols = db.books.find({ "status": True, "$text": { "$search": query } })

    books = []

    for x in cols:
        books.append(x)

    return jsonify({
        'books': books
    })


def get_language_with_other(lang):
    def_lang = ["English", "Indonesian"]

    for l in lang:
        if l in def_lang:
            def_lang.remove(l)

    print(def_lang)
    return def_lang

def get_query_filter(genre, languages, from_date, until_date):
    query = {"enabled": True}

    if not genre and not languages and not from_date and not until_date:
        return query

    if genre:
        query = {**query, "genres": {"$in": genre}}

    if languages:
        if 'other' not in languages:
            query = {**query, "language": {"$in": languages}}
        else:
            query = {**query, "language": {"$nin": get_language_with_other(languages)}}

    if from_date:
        query = {**query, "published_date": {"$gte": datetime(int(from_date), 1, 1)}}

        if until_date:
            query = {**query, "published_date": {**query['published_date'], "$lte": datetime(int(until_date), 12, 12)}} 

    return query

def get_genres():
    cols = db.books.find()

    books = []
    genres = []

    for x in cols:
        books.append(x)

    for book in books:
        for genre in book['genres']:
            genres.append(genre)

    genres = list(set(genres))
    genres.sort()
    
    return genres