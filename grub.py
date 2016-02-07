import sys; sys.path.insert(0, 'lib') # this line is necessary for the rest
import os                             # of the imports to work!

import web
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import sqlitedb
from sets import Set

from fractions import gcd

urls = (
    '/hello', 'hello', '/view', 'view', '/user', 'user', '/cookbook', 'cookbook', '/search', 'search','/upload_page', 'upload_page'
)
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'sessionUser': ""})
render = web.template.render('templates/')
class hello:        
    def GET(self):
        all_recipes = sqlitedb.getAllRecipes()
        all_photos = sqlitedb.getAllPhotos()
        session.sessionUser = 'blubbo'
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

#added by valerie for reviews
    def POST(self):
        post_params = web.input()
        recipeID = post_params['recipeID']
        if 'review' in post_params:
            sqlitedb.addRecipeReview(recipeID, "blubbo",post_params['review'], int(post_params['stars']))

            #need to update overall rating now
            ratings = sqlitedb.getReviews(recipeID)
            counter = 0.0
            total = 0
            for r in ratings:
                total += r['Rating']
                counter += 1.0
            new_rating = total/counter
            sqlitedb.updateRating(recipeID, new_rating)

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

class search:
    def GET(self):
        return render_template('search_recipes.html')

    def POST(self):
        post_params = web.input()
        recipeID = post_params['recipeID']
        userID = post_params['userID']
        recipeName = post_params['recipeName']
        completionTime = post_params['completionTime']
        ingredients = post_params['ingredients'].split()
        categories = post_params['categories'].split()
        tags = post_params['tags'].split()
        
        final_search_results = sqlitedb.searchRecipes(recipeID, userID, recipeName, completionTime, ingredients, categories, tags)
        return render_template('search_recipes.html', search_results = final_search_results)


#adam's stuff
class upload_page:
    def GET(self):
        return render.upload_page()
    def POST(self):
        recipeID = sqlitedb.assignRecipeID()
        data = web.input()

        sqlitedb.addRecipe(recipeID,
                "billy", #TODO: ADD THE USER ID
                0,
                data.name,
                data.description,
                data.time,
                data.servings,
                data.spicy,
                data.diff)

        tags = data.tags
        tags = tags.split()
        for tag in tags:
            sqlitedb.addRecipeTags(recipeID, tag)

        numIngredients = int(data.numIngredients)
        for i in range(numIngredients):
            ingredient = data["ingredientIngredient" + str(i)]
            unit = "none"
            if ("ingredientUnit" + str(i)) in data:
                unit = data["ingredientUnit" + str(i)]
            numerator = 1
            denominator = 1
            if ("ingredientQuantity" + str(i)) in data:
                quantity = data["ingredientQuantity" + str(i)]
                if '/' in quantity:
                    quantityFraction = quantity.split('/')
                    numerator = int(quantityFraction[0])
                    denominator = int(quantityFraction[0])
                elif '.' in quantity:
                    quantityDecimal = float(quantity)
                    while (quantityDecimal % 1) != 0:
                        quantityDecimal *= 10
                        denominator *= 10
                    numerator = int(quantityDecimal)
                    factor = gcd(numerator, denominator)
                    numerator /= factor
                    denominator /= factor
                elif quantity != "":
                    numerator = int(quantity)
            sqlitedb.addRecipeIngredients(recipeID, ingredient, numerator, denominator, unit)

        numInstructions = int(data.numInstructions)
        for i in range(numInstructions):
            if ("instruction" + str(i)) in data:
                sqlitedb.addRecipeInstruction(recipeID, i + 1, data["instruction" + str(i)])

        numImages = int(data.numImages)
        for i in range(numImages):
            if ("image" + str(i)) in data:
                sqlitedb.addRecipePhotos(recipeID, data["image" + str(i)])

        print data
        if  'categoriesBR' in data:
            sqlitedb.addRecipeCategories(recipeID, "breakfast")
        if 'categoriesLU' in data:
            sqlitedb.addRecipeCategories(recipeID, "lunch")
        if 'categoriesDI' in data:
            sqlitedb.addRecipeCategories(recipeID, "dinner")
        if 'categoriesSA' in data:
            sqlitedb.addRecipeCategories(recipeID, "savory")
        if 'categoriesSW' in data:
            sqlitedb.addRecipeCategories(recipeID, "sweet")
        if 'categoriesVE' in data:
            sqlitedb.addRecipeCategories(recipeID, "vegetarian")
        if 'categoriesGF' in data:
            sqlitedb.addRecipeCategories(recipeID, "gluten free")

        recipe = sqlitedb.getRecipe(recipeID)
        instructions = sqlitedb.getInstructions(recipeID)
        ingredients = sqlitedb.getIngredients(recipeID)
        tags = sqlitedb.getTags(recipeID)
        photos = sqlitedb.getPhotos(recipeID)
        categories = sqlitedb.getCategories(recipeID)
        reviews = sqlitedb.getReviews(recipeID)
        return render_template('view_recipe.html', recipe = recipe, instructions = instructions, ingredients = ingredients, tags = tags, photos = photos, categories = categories, reviews = reviews)


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