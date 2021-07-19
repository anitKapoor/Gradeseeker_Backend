# Import necessary packages
from flask import Flask, request, redirect, url_for, session
from flaskext.mysql import MySQL

# Create vars for Flask and MySQL
app = Flask(__name__)
sql_var = MySQL()
sql_var.init_app(app)

# App route for /login.
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        user_id = request.form["user_id"]
        user_pass = request.form["user_pass"]

        session["user_id"] = user_id

# App route for logout.
@app.route("/logout")
def logout():
    return "Hello, World!"

# App route for /signup.
@app.route("/signup", methods=["POST"])
def signup():
    return "Hello, World!"

# App route for searching courses by course code, i.e. CS411, ECE220, and so on.
@app.route("/search/class/<course_code>", methods=["GET"])
def get_course(course_code):
    return "Hello, World!"

# App route for searching classes by professor name.
@app.route("/search/professor/<professor_name>", methods=["GET"])
def get_professor(professor_name):
    return "Hello, World!"

# App route for searching classes by CRN (course registration number).
@app.route("/search/crn/<crn_val>", methods=["GET"])
def get_class_by_crn(crn_val):
    return "Hello, World!"

# App route to view and update a user's profile.
@app.route("/userprofile", methods=["GET", "POST"])
def get_profile():
    return "Hello, World!"
