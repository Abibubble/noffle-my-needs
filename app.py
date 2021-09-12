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
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()

    noffles = mongo.db.noffles.find()
    return render_template('landing.html', name=name, noffles=noffles, user=user)


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
                return redirect(url_for('set_noffles'))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for('login'))

        else:
            # Username does not exist
            flash("Incorrect Username and/or Password")
            return render_template("login.html")

    return render_template("login.html")


@app.route('/logout')
def logout():
    # Find if a user is logged in for the navbar
    print("*", session["user"], "*")
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
        # For some reason, this doesn't work without the print statement below.
        # No clue why. Please tell Abi if you figure out why, or how to fix it!!
        print(user)
        flash("You have been logged out")
    except BaseException:
        user = mongo.db.users.find()
        flash("You're already logged out!")
        return redirect(url_for("landing"))
    # Remove user from session cookies and log out
    session.pop("user")
    return redirect(url_for("landing"))


@app.route('/register', methods=["GET", "POST"])
def register():
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()

    if request.method == 'POST':
        # Set variables
        username = request.form.get("username").lower()
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")
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
            "is_admin": False,
            "noffles": []
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Hi, {}. Welcome to Noffle My Needs.".format(
                        request.form.get("username").capitalize()))

        return render_template("set_noffles.html", noffles=noffles, user=user)

    return render_template('register.html')


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()

    noffles = mongo.db.noffles.find()
    if session["user"]:
        return render_template(
            "profile.html", noffles=noffles, user=user)
    else:
        flash("You need to be logged in to access this page")
        return redirect(url_for("login"))
    return redirect(url_for("landing"))


@app.route('/office')
def office(name=None):
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()

        flash("You need to be logged in to access this page")
        return redirect(url_for("login"))
    noffles = mongo.db.noffles.find()
    return render_template('office.html', name=name, noffles=noffles, user=user)


@app.route('/manage_noffles')
def manage_noffles(name=None):
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page")
        return redirect(url_for("login"))

    # Show categories to admin user
    if user["is_admin"] is False:
        flash("You need to be an admin to access this page")
        return redirect(url_for("office"))
    else:
        noffles = mongo.db.noffles.find()
        return render_template(
            'manage_noffles.html', name=name, noffles=noffles, user=user)
    return redirect(url_for("login"))


@app.route('/manage_users')
def manage_users(name=None):
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page")
        return redirect(url_for("login"))

    # Show users to admin only
    if user["is_admin"] is False:
        flash("You need to be an admin to access this page")
        return redirect(url_for("office"))

    noffles = mongo.db.noffles.find()
    users = mongo.db.users.find()
    return render_template(
        'manage_users.html', name=name, noffles=noffles,
        users=users, user=user)


@app.route('/set_noffles')
def set_noffles(name=None):
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page")
        return redirect(url_for("login"))
    noffles = mongo.db.noffles.find()
    return render_template(
        'set_noffles.html', name=name, noffles=noffles, user=user)


@app.route('/add_noffle/<noffle_id>')
def add_noffle(noffle_id):
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page")
        return redirect(url_for("login"))

    # Add noffle to their profile
    noffles = mongo.db.noffles.find()
    noffle = mongo.db.noffles.find_one({"_id": noffle_id})
    user = mongo.db.users.find_one({"username": session["user"]})
    user["noffles"].append(noffle)
    return render_template(
        'set_noffles.html', noffles=noffles, user=user)


@app.route('/delete_account/<username>')
def delete_account(username):
    # Find if a user is logged in
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page")
        return redirect(url_for("login"))

    # Allow user to delete their own account
    mongo.db.users.remove({"username": username})
    flash("User Successfully Deleted")
    session.pop("user")
    return redirect(url_for("landing"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
