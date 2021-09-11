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
    return render_template('index.html', name=name, noffles=noffles)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('trying to login')
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return render_template("index.html")
            else:
                # invalid passwword match
                print("Incorrect Username and/or Password")
                """
                Add redirect url for profile page once it is created
                """
                return render_template("login.html")

        else:
            # username does not exist
            print("Incorrect Username and/or Password")
            return render_template("login.html")

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop("user")
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # check if the username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            print("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        print(session)
        print("Hi, {}. Welcome to Noffle My Needs.".format(
                        request.form.get("username").capitalize()))
        """
        Add redirect url for profile page once it is created
        """
        return render_template("index.html")
    return render_template('register.html')


@app.route('/admin')
def admin(name=None):
    return render_template('admin.html', name=name)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
