import os
from flask import (Flask, flash, render_template, redirect, request, session,
                   url_for)
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
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()

    noffles = mongo.db.noffles.find()
    return render_template('landing.html',
                           name=name,
                           noffles=noffles,
                           user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for('set_noffles'))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password", 'error')
                return redirect(url_for('login'))

        else:
            # Username does not exist
            flash("Incorrect Username and/or Password", 'error')
            return render_template("login.html")

    return render_template("login.html")


@app.route('/logout')
def logout():
    # Find if a user is logged in for the navbar
    print("*", session["user"], "*")
    
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
        """
        Check the noffles that are not permament and delete from 
        the user's noffles when logout
        """
        for noffle in user["noffles"]:
            my_noffles = mongo.db.noffles.find_one({"_id": ObjectId(noffle)})
            if not my_noffles['permanent']:
                noffle_id = str(my_noffles['_id'])
                mongo.db.users.update({'_id': ObjectId(user['_id'])}, {'$pull': {'noffles': noffle_id}})
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
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()

    noffles = mongo.db.noffles.find()

    if request.method == 'POST':
        # Set variables for form
        username = request.form.get("username").lower()
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")
        # Check if the username already exists in database
        existing_user = mongo.db.users.find_one({"username": username})

        if existing_user:
            flash("Username already exists", 'error')
            return redirect(url_for("register"))

        if password != password_confirm:
            flash("Oh no! Your passwords don't match", 'error')
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(password),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "pronouns": request.form.get("pronouns").lower(),
            "image_no": request.form.get("image_no"),
            "is_admin": False,
            "noffles": [],
            "panic": False
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Hi, {}. Welcome to Noffle My Needs.".format(
            request.form.get("username").capitalize()))
        return render_template("set_noffles.html",
                               noffles=noffles,
                               user=user,
                               user_noffles={})

    return render_template('register.html', user=user)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page", 'error')
        return redirect(url_for("login"))

    # Display all noffles the user has set
    noffles = []
    try:
        for noffle in user["noffles"]:
            my_noffles = mongo.db.noffles.find_one({"_id": ObjectId(noffle)})
            noffles.append(my_noffles)
    except BaseException:
        noffles = []

    if session["user"]:
        return render_template("profile.html", noffles=noffles, user=user)
    else:
        flash("You need to be logged in to access this page", 'error')
        return redirect(url_for("login"))

    return redirect(url_for("landing"))


@app.route('/update_user/<user_id>', methods=["GET", "POST"])
def update_user(user_id):
    # Find the logged in user for navlinks
    try:
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page", 'error')
        return redirect(url_for("login"))

    # Display all noffles the user has set
    noffles = []
    try:
        for noffle in user["noffles"]:
            my_noffles = mongo.db.noffles.find_one({"_id": ObjectId(noffle)})
            noffles.append(my_noffles)
    except BaseException:
        noffles = []

    if request.method == 'POST':
        # Set variables for the form
        username = request.form.get("username").lower()
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        if password != password_confirm:
            flash("Oh no! Your passwords don't match", 'error')
            return redirect(url_for("profile", username=username))

        update_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(password),
            "pronouns": request.form.get("pronouns").lower(),
            "image_no": request.form.get("image_no"),
        }
        mongo.db.users.update_one({"_id": ObjectId(user["_id"])},
                                  {'$set': update_user})

    return redirect(url_for("profile", username=username))


@app.route('/office')
def office(name=None):
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page", 'error')
        return redirect(url_for("login"))

    users = mongo.db.users.find()
    noffles = mongo.db.noffles.find()

    # Display all noffles the user has set
    noffle_dict = {}
    for managed_user in users:
        noffles_list = []
        for noffle in managed_user['noffles']:
            my_noffles = mongo.db.noffles.find_one({"_id": ObjectId(noffle)})
            noffles_list.append(my_noffles)
        noffle_dict[str(managed_user['username'])] = noffles_list

    users = mongo.db.users.find()
    noffles = mongo.db.noffles.find()
    return render_template('office.html',
                           name=name,
                           noffles=noffles,
                           user=user,
                           users=users,
                           noffle_dict=noffle_dict)


@app.route('/manage_noffles')
def manage_noffles(name=None):
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page", 'error')
        return redirect(url_for("login"))

    # Show categories to admin user
    if user["is_admin"] is False:
        flash("You need to be an admin to access this page", 'error')
        return redirect(url_for("office"))
    else:
        noffles = mongo.db.noffles.find()
        return render_template('manage_noffles.html',
                               name=name,
                               noffles=noffles,
                               user=user)
    return redirect(url_for("login"))


@app.route('/manage_users')
def manage_users(name=None):
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page", 'error')
        return redirect(url_for("login"))

    # Show users to admin only
    if user["is_admin"] is False:
        flash("You need to be an admin to access this page", 'error')
        return redirect(url_for("office"))

    users = mongo.db.users.find()

    # Display all noffles the user has set
    noffle_dict = {}
    for managed_user in users:
        noffles_list = []
        for noffle in managed_user['noffles']:
            my_noffles = mongo.db.noffles.find_one({"_id": ObjectId(noffle)})
            noffles_list.append(my_noffles)
        noffle_dict[str(managed_user['username'])] = noffles_list

    noffles = mongo.db.noffles.find()
    users = mongo.db.users.find()

    return render_template('manage_users.html',
                           name=name,
                           noffles=noffles,
                           users=users,
                           user=user,
                           noffle_dict=noffle_dict)


@app.route("/admin_toggle/<user_id>")
def admin_toggle(user_id):
    # Allow admin to give or remove admin rights on other users
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

    if user["is_admin"] is False:
        mongo.db.users.update({"_id": ObjectId(user_id)},
                              {"$set": {
                                  "is_admin": True
                              }})
        flash("User Admin Rights Added")
    else:
        mongo.db.users.update({"_id": ObjectId(user_id)},
                              {"$set": {
                                  "is_admin": False
                              }})
        flash("User Admin Rights Removed")

    return redirect(url_for("manage_users"))


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    # Allow admin user to delete other users
    print(">>>>>>", user_id)
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("manage_users"))


@app.route("/delete_noffle/<noffle_id>")
def delete_noffle(noffle_id):
    # Allow admin user to delete noffles
    flash(f'Noffle Successfully Deleted')
    mongo.db.noffles.remove({"_id": ObjectId(noffle_id)})
    users = mongo.db.users.find()

    # Remove the deleted noffle from all users
    for user in users:
        for noffle in user["noffles"]:
            if noffle == noffle_id:
                mongo.db.users.update(
                    {'_id': ObjectId(user['_id'])}, {'$pull': {'noffles': noffle_id}})

    flash("Noffle Successfully Deleted")

    return redirect(url_for("manage_noffles"))


@app.route('/set_noffles')
def set_noffles(name=None):
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page", 'error')
        return redirect(url_for("login"))

    noffles = mongo.db.noffles.find()
    user_noffles = user['noffles']

    return render_template('set_noffles.html',
                           name=name,
                           noffles=noffles,
                           user=user,
                           user_noffles=user_noffles)


@app.route('/add_noffle/<noffle_id>')
def add_noffle(noffle_id):
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page", 'error')
        return redirect(url_for("login"))

    # Find noffle and user
    noffles = mongo.db.noffles.find()
    noffle = mongo.db.noffles.find_one({"_id": noffle_id})
    user = mongo.db.users.find_one({"username": session["user"]})
    current_noffle = mongo.db.noffles.find_one({"_id": ObjectId(noffle_id)})

    # Check if noffle is selected, and add it to profile if it isn't
    if noffle_id in user['noffles']:
        flash(f'Noffle {current_noffle["name"]} removed from your Noffles')
        if current_noffle["name"] == 'Panic button':
            mongo.db.users.update({"_id": ObjectId(user["_id"])},
                                  {"$set": {
                                      "panic": False
                                  }})
        mongo.db.users.update({'_id': ObjectId(user['_id'])},
                              {'$pull': {
                                  'noffles': noffle_id
                              }})
        return redirect(url_for("set_noffles", noffles=noffles, user=user))
    else:
        flash(f'Noffle {current_noffle["name"]} added to your Noffles')
        if current_noffle["name"] == 'Panic button':
            mongo.db.users.update({"_id": ObjectId(user["_id"])},
                                  {"$set": {
                                      "panic": True
                                  }})
        mongo.db.users.update({'_id': ObjectId(user['_id'])},
                              {'$push': {
                                  'noffles': noffle_id
                              }})
        return redirect(url_for("set_noffles", noffles=noffles, user=user))

    return render_template('set_noffles.html', noffles=noffles, user=user)


@app.route('/new_noffle', methods=["GET", "POST"])
def new_noffle():
    # Find if a user is logged in for navlinks
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

    if request.method == 'POST':
        # Set variables for form
        noffle_name = request.form.get("name")
        # Check if the username already exists in database
        existing_noffle = mongo.db.noffles.find_one({"name": noffle_name})

        if existing_noffle:
            flash(f'Noffle {noffle_name} already exists')
            return redirect(url_for("manage_noffles"))

        new_noffle_addition = {
            "name": noffle_name,
            "description": request.form.get("description"),
            "permanent": request.form.get("permanent"),
            "private": request.form.get("private"),
            "icon": request.form.get("icon")
        }
        mongo.db.noffles.insert_one(new_noffle_addition)

        # Put the new user into 'session' cookie
        flash(f'Noffle {noffle.name} has been added')
        return render_template("manage_noffles.html",
                               noffles=noffles,
                               user=user)

    return render_template("manage_noffles.html", noffles=noffles, user=user)

@app.route('/delete_account/<username>')
def delete_account(username):
    # Find if a user is logged in for navlinks
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        user = mongo.db.users.find()
        flash("You need to be logged in to access this page", 'error')
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
