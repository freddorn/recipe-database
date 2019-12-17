# Recipe Database

View website on [Heroku](https://recipe-data.herokuapp.com)

A recipe database where viewers can search and view recipes. Users can also create an account, 
where they can add, edit or delete their own recipes.
 
## UX
 
A simple uncluttered layout, to make it easy for users to navigate the site.
The information is presented in an easy to use manner. The recipe information
rests on a transparent background with a background image behind the main section
of the website.

### User Stories

* I would like to search and view recipes by keywords.
* To add my own recipes into the database.
* Be able to edit and delete my own recipes.
* I like that my own recipes are protected and are only able to be edited or    
  deleted by myself.


**Wireframes** can be viewed [here](https://github.com/freddorn/recipe-database/tree/master/static/wireframes)

## Features
 
 ### Existing Features

* A search field to search for recipes by keyword. It searches any word in the     database.
* Search by recipe category on the categories page.
* Register and login feature, that only allows users to add recipes when logged in
  and prevents the editing or deleting of other user's recipes.
* A form for users to add their own recipes, to the database.
* The All Recipes page, that will show all the recipes, or just recipes that fit a
  user's search criteria.
* A View Recipe page that has information about each recipe, including ingredients
  and preparation instructions.
* The ability of users to edit or delete their own recipes.
* A warning that is displayed, when the delete button is clicked, to alert the user
  in case the button was pushed accidentally.

### Features Left to Implement

* User email authentication, for a user to change their password.
* A way for the administrator to have control of all entries and database content
  without having to log into the Mongodb Atlas console.
* Pagination so the number of recipe results doesn't become too long, as the
  database grows.

### Database Structure




| Title | Key in db | form type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Name | username | text | string
Password | password | text | string



| Title | Key in db | form type | Data type |
--- | --- | --- | --- 
Recipe ID | _id | None | ObjectId 
Username | username |text | string
Category Name | category_name | text | string
Recipe Name | recipe-name | text | string
Ingredients | ingredients | text | string
Preparation | preparation | text | string



## Technologies Used

### Languages
* HTML 
* CSS 
* Javascript
* Python
### Tools
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is the database for this project.
- [GitHub](https://github.com/) to store and share all project code remotely.
- [Materialize](https://materializecss.com//) Was used as the basis for the site's design and responsiveness.

-  [Heroku](https://www.heroku.com/) Was used to deploy the project.
-  [unittest](https://docs.python.org/2/library/unittest.html) Was used for automated testing of the Python code.

 

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Google Fonts](https://fonts.google.com/) To style the website fonts.
- [PyMongo](https://api.mongodb.com/python/current/) To make communication between 	Python and MongoDB possible.
- [Flask](https://flask.palletsprojects.com/en/1.0.x/) To construct and render 	pages.
- [Jinja](http://jinja.pocoo.org/docs/2.10/) For simplify displaying data from the 	backend of this project smoothly and effectively in html.



## Testing

### Automated Tests

Conducted automated testing of the app routes with unittests. The testing file is named testing.py in the root directory. Run the tests by entering ```python3 testing.py``` in the terminal.

  
### Manual Tests

Performed manual tests of the application as follows:

1. Cross-browser and Device Compatibility
    1. Tested the app on Chrome, Edge, Firefox Opera and Safari browsers to verify   that it works on all of them.
    2. Tested the app on a desktop, laptop, tablet and smartphone to verify that it works on all devices.

2. Responsiveness
    1. View the app in responsive mode with Chrome Developer Tools to check that the size and position of elements adjusts correctly.
    2. View the app on a desktop, laptop, tablet and smartphone to verify that it displays correctly.

3. Registration
    1. Navigate to the registration page.
    2. Enter a username and password.
    3. Verify that I see text at the top of the page saying that am logged in under that username.
    4. Verify that I can add recipes and edit and delete recipes submitted under that username, and that I can't edit or delete other users' recipes.
    5. Verify that, when I click on the "Your Recipes" link in the navbar, that I see the list of that user's recipes and no others.
    6. Click on the Logout link in the navbar and check that I'm logged out.
    7. Enter a username that's already in the database.
    8. Verify that a message appears saying that the username already exists.
     
4. Login
    1. Navigate to the 'Login' page.
    2. Enter a correct username and password.
    3. Verify that I see text at the top of the page saying that am logged in under that username.
    4. Verify that I can add, edit and delete recipes submitted under that username and that I can't edit or delete, other user's recipes.
    5. Verify that when I click on the "Your Recipes" link in the navbar, I see the list of that user's recipes and no others.
    6. Click on the Logout link in the navbar and check that I'm logged out.
    7. Enter a username that's not in the database and a password.
    8. Verify that I see a message saying that I've entered an incorrect username/password combination.
    9. Enter a username that's in the database and an incorrect password.
    10. Verify that I see a message saying that I've entered an incorrect username/password combination.

5. Adding Recipes
    1. Click on the "Add a Recipe" link in the navbar.
    2. Verify that the form appears correctly.
    3. Attempt to submit the form with required fields blank and check that I'm prompted to fill them.
    4. Submit a fully completed form.
    5. Click on the link to the new recipe in the list of recipes that appears.
    6. Verify that the page showing that recipe loads correctly, with all entered details appearing.
    7. Verify that all the recipe details have been saved in the database.

6. Searching for Recipes
    1. Enter various search terms in the search bar.
    2. Verify that all recipes with those words, and only recipes with those words, are displayed in the results.
    3. Click on each image on the 'Categories' page.
    4. Verify that all recipes in that category, and only recipes in that category, are displayed in the results.
    
 
7. Viewing Recipes
    1. Click on the 'Home' link in the navbar.
    2. Verify that all recipes in the database are listed on the page that loads.
    3. Click on each recipe in the list.
    4. Verify that all the recipe details are displayed correctly on the 'View Recipe' page that loads.

8. Editing Recipes
    1. Click on the 'Edit' button at the bottom of a page displaying a recipe.
    2. Verify that the form for editing the recipe loads.
    3. Edit the recipe details.
    4. Click the 'Submit' button.
    5. Verify that the recipe reloads and the edits have been saved to the database.
    6. Click on the 'Edit' button at the bottom of a page displaying a recipe.
    7. Verify that the form for editing the recipe loads.
    8. Edit the recipe details.
    8. Click the 'Cancel' button.
    9. Verify that the recipe reloads, with none of the cancelled changes saved to the database.
    10. Repeat for all recipes.

9. Deleting Recipes
    1. Click the 'Delete' button at the bottom of the recipe display page.
    2. Verify that a warning message appears, along with buttons to cancel or confirm the deletion.
    3. Click 'Cancel'.
    4. Verify that the page reloads correctly.
    5. Click the 'Delete' button again.
    5. Click 'Confirm'.
    6. Verify that the recipe is deleted from the database.
    7. Repeat for all recipes.



#### Testing Tools:

* [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
    - To check the the validity of the CSS code. 
    
* [W3C Markup Validation]( https://validator.w3.org/)
    - To check the the validity of the HTML code.

#### Bugs Fixed

1. When on the Categories page and choosing Main Dishes, not all recipes would
    be found in the search. Found that in the database, some entries had Main dishes
    vs Main Dishes.



## Deployment

To deploy the site to Heroku:

1. Create a new app app with the name recipe-data.
2. Linked the recipe-data app to its Github repository.
3. Verify that the project has an up to date Procfile and requirements.txt
4. Push the project to the Heroku remote.
5. Set the SECRET_KEY environmental variable in the Heroku config vars.
6. Set the IP to 0.0.0.0 and the PORT to 5000 in the Heroku config vars.
7. Set the MONGO_URI environmental variable in the Heroku config vars.
8. Restart all dynos.
9. Open the app on Heroku and check to ensure that it's working correctly.


### Running the Code Locally

1. Under the repository name on GitHub, click Clone or download.
2. In the Clone with HTTPs section, click the icon beside the URL to copy the clone URL for the repository.
3. Change the current working directory to the location where you want the cloned directory to be made.
4. Type git clone, and then paste the URL you copied in Step 2.
5. Press Enter. Your local clone will be created.
6. Set up a virtual environment.
7. Install the packages in requirements.txt by typing pip3 install -r requirements.txt in the CLI.
8. Set the IP address to 127.0.0.1 and the PORT to 5000.


## Credits

### Content and Media

- The category image photos used for this site, were obtained from [Pxhere](https://pxhere.com/en/)
- The recipes used to start the database were obtained from [Cookbooks.com](http://www.cookbooks.com/cookbooks-index.aspx)



### Acknowledgements

- I received inspiration for this project from [Cookbooks.com](http://www.cookbooks.com/cookbooks-index.aspx)
- The Slack community, where I have learned a great deal, reading through many posts.
- My mentor Sebastian Immel.
- W3SCHOOLS website for easy explanation of the code.
- Stack Overflow, a good source of knowledge.