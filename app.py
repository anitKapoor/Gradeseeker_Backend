# Import necessary packages
from flask import Flask, request, redirect, url_for, session
from flaskext.mysql import MySQL

# Create vars for Flask and MySQL
app = Flask(__name__)
sql_var = MySQL()
sql_var.init_app(app)

# App route for /login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return "Hello, World!"

# App route for /signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return "Hello, World!"