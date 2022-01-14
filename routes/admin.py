from decorators import admin_required
from app import app, db
from flask import render_template

@app.route('/admin')
@admin_required
def admin_dashboard():
    return render_template('dashboard.html', post=json.dumps(['a']))

@app.route('/admin/catalog')
@admin_required
def admin_catalog():
    return render_template('catalog.html')

@app.route('/admin/scrap')
@admin_required
def admin_scrap():
    cols = db.scrap_logs.find()

    logs = []

    for x in cols:
        logs.append(x)

    return render_template('scrap.html', logs=logs)