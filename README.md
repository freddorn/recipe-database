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

####Users Collection

| Title | Key in db | form type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Name | username | text | string
Password | password | text | string
####Recipe Collection
| Title | Key in db | form type | Data type |
--- | --- | --- | --- 
Recipe ID | _id | None | ObjectId 
Username | username |text | string
Category Name | category_name | text | string
Recipe Name | recipe-name | text | string
Ingredients | ingredients | text | string
Preparation | preparation | text | string



## Technologies Used




## Testing



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