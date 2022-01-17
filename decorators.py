from functools import wraps
from flask import session, redirect

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session and session['user']['role'] == 'admin':
            return f(*args, **kwargs)
        else:
            return redirect('/')
    
    return wrap

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect('/')
        else:
            return f(*args, **kwargs)
    
    return wrap