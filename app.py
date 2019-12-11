import os
from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'recipedb'
app.secret_key = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


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


""" The register and login code was inspired by Pretty Printed
https://github.com/PrettyPrinted/mongodb-user-login/blob/master/login_example.py """


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
            """ If the username is in the database, hash the password entered in the form
             and compare it with the hashed password in the database for that user"""

            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('all_recipes'))

        """ The user sees an invalid message """
        flash('Invalid username/password combination.')

    return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('all_recipes'))


@app.route('/view_recipe/<recipe_id>', methods=['GET', 'POST'])
def view_recipe(recipe_id):
    """ Display a recipe, including ingredients ad preparation"""

    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template(
        'view_recipe.html', recipe=the_recipe)


@app.route('/user_recipes')
def user_recipes():
    """A page listing the logged-in user's own recipes"""

    user = session['username']
    query = ({'username': user})
    results = mongo.db.recipes.find(query).sort('recipe_name', 1)
    return render_template('all_recipes.html',
                           recipes=results, count=results.count())


@app.route('/warning/<recipe_id>', methods=['GET', 'POST'])
def warning(recipe_id):
    """Display a warning when a user clicks the Delete button"""

    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    flash('This will permanently delete the recipe. Are you sure?')
    return render_template(
        'view_recipe.html', recipe=the_recipe)


@app.route('/delete_recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    """Delete a recipe when the user clicks the Confirm button"""

    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))


@app.route('/add_recipe')
def add_recipe():
    """Load a form for logged-in users to add a new recipe to the database"""

    """ Prevents users from submitting recipes when not logged in """
    if session:
        return render_template(
            'add_recipe.html', categories=mongo.db.categories.find())

    else:
        return redirect(url_for('login'))


@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    """Post a new recipe to the database and display it after filling in the form"""

    recipes = mongo.db.recipes
    new_recipe = {
        'recipe_name': request.form.get('recipe_name'),
        'category_name': request.form.get('category_name'),
        'ingredients': request.form.get('ingredients'),
        'preparation': request.form.get('preparation'),
        'username': session['username']
    }
    recipes.insert_one(new_recipe)
    return render_template(
        'view_recipe.html', recipe=new_recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """Load a form to edit a recipe"""

    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/submit_changes/<recipe_id>', methods=['GET', 'POST'])
def submit_changes(recipe_id):
    """Submit changes after editing"""

    mongo.db.recipes.update(
        {'_id': ObjectId(recipe_id)},
        {
            'recipe_name': request.form.get('recipe_name'),
            'category_name': request.form.get('category_name'),
            'ingredients': request.form.get('ingredients'),
            'preparation': request.form.get('preparation'),
            'username': session['username']
        })
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template(
        'view_recipe.html', recipe=the_recipe)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
