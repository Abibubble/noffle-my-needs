import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/landing')
def landing(name=None):
    noffles = mongo.db.noffles.find()
    return render_template('landing.html', name=name, noffles=noffles)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return render_template("index.html")
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for('profile'))

        else:
            # Username does not exist
            flash("Incorrect Username and/or Password")
            return render_template("login.html")

    return render_template("login.html")


@app.route('/logout')
def logout():
    # Remove user from session cookies and log out
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for("landing"))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        # Set variables
        username = request.form.get("username").lower()
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")
        print(password_confirm)
        # Check if the username already exists in database
        existing_user = mongo.db.users.find_one({"username": username})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if password != password_confirm:
            flash("Oh no! Your passwords don't match")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(password),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "pronouns": request.form.get("pronouns").lower(),
            "image_no": request.form.get("image_no"),
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Hi, {}. Welcome to Noffle My Needs.".format(
                        request.form.get("username").capitalize()))
        return render_template("set_noffles.html")
    return render_template('register.html')


@app.route("/profile", methods=["GET", "POST"])
def profile(name=None):
    noffles = mongo.db.noffles.find()

    if session["user"]:
        return render_template(
            "profile.html", noffles=noffles, user=user)

    return redirect(url_for("login"))


@app.route('/office')
def office(name=None):
    noffles = mongo.db.noffles.find()
    return render_template('office.html', name=name, noffles=noffles)


@app.route('/manage_noffles')
def manage_noffles(name=None):
    noffles = mongo.db.noffles.find()
    return render_template('manage_noffles.html', name=name, noffles=noffles)


@app.route('/manage_users')
def manage_users(name=None):
    noffles = mongo.db.noffles.find()
    users = mongo.db.users.find()
    return render_template(
        'manage_users.html', name=name, noffles=noffles, users=users)


@app.route('/set_noffles')
def set_noffles(name=None):
    noffles = mongo.db.noffles.find()
    return render_template('set_noffles.html', name=name, noffles=noffles)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
