from decorators import admin_required
from app import app, db
from flask import render_template

@app.route('/admin')
@admin_required
def admin_dashboard():
    return render_template('dashboard.html')

@app.route('/admin/catalog')
@admin_required
def admin_catalog():
    cols = db.books.find()

    books = []

    for x in cols:
        books.append(x)
    return render_template('catalog.html', books=books)

@app.route('/admin/scrap')
@admin_required
def admin_scrap():
    cols = db.scrap_logs.find()

    logs = []

    for x in cols:
        logs.append(x)

    return render_template('scrap.html', logs=logs)