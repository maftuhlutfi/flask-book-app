import os
import pathlib

import requests
from flask import Flask, jsonify, request, session, redirect, abort
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "358672265477-5nsn0pt1cimgg44f4jc6nndd9to9tf03.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:5000/user/google/callback"
)

class User:

  def start_session(self, user):
    session['logged_in'] = True
    session['user'] = user
    return jsonify({"user": user, "message": "Successfully logged in. Redirecting to homepage"}), 200

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

    if db.users.insert_one({**user, "picture": None}):
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
      return self.start_session({'id': user['_id'], 'email': user['email'], 'name': user['name'], 'picture': user['picture']})
    else:
      return jsonify({ "error": "Password is wrong" }), 401
  
  def google_login(self):
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

  def google_callback(self):
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    user = {
      "google_id": id_info.get("sub"),
      "name": id_info.get("name"),
      "email": id_info.get("email"),
      "picture": id_info.get("picture")
    }

    self.start_session(user)

    return redirect("/")
    