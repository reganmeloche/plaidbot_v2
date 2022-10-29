from functools import wraps
from flask import g, request, redirect, url_for
from src.options.web_options import WebOptions

def secret_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if request.args:
            secret = request.args['secret']
        else:
            return {"message": "Please provide the secret for this endpoint"}, 400
        # Check if secret is correct and valid
        if secret == WebOptions().secret:
            return f(*args, **kwargs)
        else:
            return {"message": "The provided secret is not valid"}, 403
    return decorator