import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo import ASCENDING
from pymongo import DESCENDING
from pymongo import TEXT

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'recipedb'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)
recipes = mongo.db.recipes

mongo.db.recipes.create_index([('$**', 'text')])
mongo.db.users.create_index([('$**', 'text')])


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("all_recipes.html",
                           recipes=recipes.find().sort('recipe_name', 1),
                           count=recipes.count())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
