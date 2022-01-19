from flask import Flask, flash, jsonify, session, redirect, request, send_from_directory
from app import app, db
from werkzeug.utils import secure_filename
import os

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/uploads/avatar', methods=['POST'])
def upload_avatar():
    # check if the post request has the file part
    if 'image' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['image']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        extension = secure_filename(file.filename).rsplit('.', 1)[1]
        print(extension)
        file.save(os.path.join('uploads/avatar', session['user']['id'] + '.' + extension))
        path = '/uploads/avatar/' + session['user']['id'] + '.' + extension
        db.users.update_one({"_id": session['user']['id']}, {"$set": {"picture": path}})
        session['user'] = {**session['user'], "picture": path}
        return jsonify({"message": "Successfully change avatar"})

@app.route('/uploads/avatar/<name>')
def get_avatar(name):
    return send_from_directory('uploads/avatar/', name)

@app.route('/uploads/books-image/<name>')
def get_book_image(name):
    return send_from_directory('uploads/books-image/', name)