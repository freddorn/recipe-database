import os
from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo import ASCENDING
from pymongo import DESCENDING
from pymongo import TEXT



app = Flask(__name__)
app.secret_key = 'h2oisg00d'

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

# The register and login routes are based on code by Pretty Printed: https://github.com/PrettyPrinted/mongodb-user-login/blob/master/login_example.py


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Allow new users to register"""

    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            # If there is no existing user with that username, encrypt the new user's password
            pw_hash = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # Decode the hashed password while keeping it encrypted so it can be stored in the MongoDB database
            db_password = pw_hash.decode("utf-8")
            # Add the username and encrypted password to the database
            users.insert(
                {'username': request.form['username'], 'password': db_password})
            # The newly registered user is logged in
            session['username'] = request.form['username']
            return redirect(url_for('all_recipes'))

        # The user sees this message if their chosen password is already in the database
        flash('That username is taken. Please try a different one.')

    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Allow registered user to log in"""

    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form['username']})

        if login_user:
            # If the username is in the database, hash the password entered in the form and compare it with the hashed password in the database for that user
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('all_recipes'))

        # The user sees this message if the username and/or password are invalid
        flash('Invalid username/password combination.')

    return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('all_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
