import sys; sys.path.insert(0, 'lib') # this line is necessary for the rest
import os                             # of the imports to work!

import web
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import sqlitedb

urls = (
    '/hello', 'hello', '/view', 'view', '/user', 'user', '/cookbook', 'cookbook',
)
app = web.application(urls, globals())

class hello:        
    def GET(self):
        all_recipes = sqlitedb.getAllRecipes()
        all_photos = sqlitedb.getAllPhotos()
    	return render_template('curr_time.html', all_recipes = all_recipes, all_photos = all_photos)

class view:
    def GET(self):
        post_params = web.input()
        recipeID = 0
        if 'recipeID' in post_params:
            recipeID = post_params['recipeID']
        recipe = sqlitedb.getRecipe(recipeID)
        instructions = sqlitedb.getInstructions(recipeID)
        ingredients = sqlitedb.getIngredients(recipeID)
        tags = sqlitedb.getTags(recipeID)
        photos = sqlitedb.getPhotos(recipeID)
        categories = sqlitedb.getCategories(recipeID)
        reviews = sqlitedb.getReviews(recipeID)
        return render_template('view_recipe.html', recipe = recipe, instructions = instructions, ingredients = ingredients, tags = tags, photos = photos, categories = categories, reviews = reviews)

class user:
    def GET(self):
        post_params = web.input()
        userID = None
        userRecipes = None
        userAboutMe = None
        userFollowers = None
        userFollowing = None
        userCookbooks = None
        if 'userID' in post_params:
            userID = post_params['userID']
            userRecipes = sqlitedb.getUserRecipes(userID)
            userAboutMe = sqlitedb.getAboutMe(userID)
            userFollowers = sqlitedb.getFollowers(userID)
            userFollowing = sqlitedb.getFollowing(userID)
            userCookbooks = sqlitedb.getCookbooks(userID)
        return render_template('view_user.html', userID = userID, userRecipes = userRecipes, userAboutMe = userAboutMe, userFollowers = userFollowers, userFollowing = userFollowing, userCookbooks = userCookbooks)

class cookbook:
    # THIS IS NOT COMPLETE YET - 1/31 at 4:28pm
    def GET(self):
        post_params = web.input()
        cookbookID = None
        cookbookRecipes = None
        if 'cookbookID' in post_params:
            cookbookID = post_params['cookbookID']
            cookbookRecipes = sqlitedb.getCookbooks_recipes(cookbookID)
        return render_template('view_cookbook.html', cookbookID = cookbookID)


# helper method to render a template in the templates/ directory
#
# `template_name': name of template file to render
#
# `**context': a dictionary of variable names mapped to values
# that is passed to Jinja2's templating engine
#
# See curr_time's `GET' method for sample usage
#
# WARNING: DO NOT CHANGE THIS METHOD
def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(autoescape=True,
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            extensions=extensions,
            )
    jinja_env.globals.update(globals)

    web.header('Content-Type','text/html; charset=utf-8', unique=True)

    return jinja_env.get_template(template_name).render(context)

if __name__ == "__main__":
    app.run()