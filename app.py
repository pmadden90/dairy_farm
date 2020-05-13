import os
import math
from jinja2 import escape
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from flask_bootstrap import Bootstrap
from os import path
if path.exists("env.py"):
    import env
from werkzeug.security import generate_password_hash, check_password_hash


#App Config     

app = Flask(__name__)

#DB Collections
MONGODB_URI = os.environ.get("MONGO_MOO")
DBS_NAME = "dairy_farm"
COLLECTION_NAME = "milk"
app.config["MONGO_URI"] = os.getenv("MONGO_PM_MONGO")
app.secret_key = os.getenv("SECRET_KEY")
mongo = PyMongo(app)
users = mongo.db.users


# Routes
# Homepage
@app.route('/')
def homepage():
    return render_template("index.html")

    # import pdb; pdb.set_trace()

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)