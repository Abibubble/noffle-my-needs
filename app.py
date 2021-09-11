from flask import Flask, redirect, render_template
from flask_pymongo import PyMongo

# for accessing the databse uri from Heroku
import os

app = Flask(__name__)

# connect to the database with Heroku env variables
# app.config["MONGO_DBNAME"] = "<insert db name>"
# app.config["MONGO_URI"] = os.getenv("MONGO_URI")


@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


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