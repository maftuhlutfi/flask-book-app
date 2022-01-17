from datetime import datetime
from flask import Flask, render_template, jsonify, session, redirect, request
from app import app, db

@app.route('/books')
def books():
    sort_name, sort_mode = request.args.get('sort').split(' ') if request.args.get('sort') != None else ['', 'dsc']
    languages =  request.args.get('languages').split(',') if request.args.get('languages') != None else None
    from_date = request.args.get('from')
    until_date = request.args.get('until')

    if 'logged_in' not in session and (sort_name or languages or from_date or until_date):
        return redirect('/login?from=filter-sort')

    field = 'published_date'

    if sort_name != 'date' and sort_name != '':
        field = sort_name

    query_filter = get_query_filter(languages, from_date, until_date)
    
    cols = db.books.find(query_filter) 

    cols.sort(field, -1 if sort_mode == 'dsc' else 1)

    books = []

    for x in cols:
        books.append(x)

    languages = []

    for book in books:
        if book['language'] not in languages:
            languages.append(book['language'])

    return render_template('books.html', books=books, languages=languages)
    
@app.route('/books/<string:book_id>')
def book(book_id):
    if 'logged_in' not in session:
        return redirect('/login?from=filter-sort')

    book = db.books.find_one({ "_id": book_id })

    return render_template('book.html', book=book)

def get_language_with_other(lang):
    def_lang = ["English", "Indonesian"]

    for l in lang:
        if l in def_lang:
            def_lang.remove(l)

    print(def_lang)
    return def_lang

def get_query_filter(languages, from_date, until_date):
    query = {}

    if not languages and not from_date and not until_date:
        return {}

    if languages:
        if 'other' not in languages:
            query = {"language": {"$in": languages}}
        else:
            query = {"language": {"$nin": get_language_with_other(languages)}}

    if from_date:
        query = {**query, "published_date": {"$gte": datetime(int(from_date), 1, 1)}}

        if until_date:
            query = {**query, "published_date": {**query['published_date'], "$lte": datetime(int(until_date), 12, 12)}} 

    return query