from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class User:

  def start_session(self, user):
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    data = request.get_json(silent=True)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      **data
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.users.insert_one({**user, "image": None}):
      return jsonify({"message": "Signup success. Please login."})

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):
    data = request.get_json(silent=True)

    user = db.users.find_one({
      "email": data['email']
    })

    if not user:
      return jsonify({ "error": "Email is not found" }), 401

    if user and pbkdf2_sha256.verify(data['password'], user['password']):
      return self.start_session({'id': user['_id'], 'email': user['email'], 'name': user['name'], 'image': user['image']})
    else:
      return jsonify({ "error": "Password is wrong" }), 401
    