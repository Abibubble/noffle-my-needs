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


@app.route('/login')
def login(name=None):
    return render_template('login.html', name=name)


@app.route('/logout')
def logout(name=None):
    return render_template('logout.html', name=name)


@app.route('/register')
def register(name=None):
    return render_template('register.html', name=name)


@app.route('/admin')
def admin(name=None):
    return render_template('admin.html', name=name)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)