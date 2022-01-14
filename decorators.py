from functools import wraps
from flask import session, redirect

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session and 'is_admin' in session['user'].keys():
            if session['user']['is_admin']:
                return f(*args, **kwargs)
            else:
                return redirect('/')
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