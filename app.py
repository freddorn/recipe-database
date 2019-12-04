import os
from flask import Flask, render_template, redirect, request, session, url_for
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

"""List either all recipes in the database or search results"""


@app.route('/')
@app.route('/all_recipes', methods=['GET', 'POST'])
def all_recipes():

    return render_template('all_recipes.html',
                           recipes=recipes.find().sort('recipe_name', 1),
                           count=recipes.count())

    """List recipes by category"""


@app.route('/all_recipes_by_cat/<category_name>', methods=['GET', 'POST'])
def all_recipes_by_cat(category_name):

    results = recipes.find(
        {'category_name': category_name}).sort('recipe_name', 1)
    return render_template('all_recipes.html',
                           recipes=results, count=results.count())


@app.route('/search', methods=['GET', 'POST'])
def search():
    """Search for a recipe by keywords"""

    keywords = request.form.get('search')
    query = ({'$text': {'$search': keywords}})
    results = mongo.db.recipes.find(query)
    return render_template('all_recipes.html',
                           recipes=results, count=results.count())


@app.route('/categories', methods=['GET', 'POST'])
def categories():
    return render_template('categories.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
