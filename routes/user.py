from flask import Flask
from app import app
from models.user import User

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/user/google')
def google_login():
  return User().google_login()

@app.route('/user/google/callback')
def google_callback():
  return User().google_callback()