__author__ = 'bhushan'

# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, session, redirect, url_for

# Define the blueprint: 'auth', set its url prefix: app.url/auth
home = Blueprint('home', __name__, url_prefix='/')

# Set the route and accepted methods
@home.route('/', methods=['GET', 'POST'])
def index():
    # If sign in form is submitted
    #form = LoginForm(request.form)
    #print( "/home/index")
    return render_template("home/index.html")