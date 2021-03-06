import sys; sys.path.insert(0, 'lib') # this line is necessary for the rest
import os                             # of the imports to work!

import web
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import sqlitedb
from sets import Set

from fractions import gcd

urls = (
    '/hello', 'hello', '/view', 'view', '/user', 'user', '/cookbook', 'cookbook', '/search', 'search', '/upload_page', 'upload_page', '/search_users', 'search_users', '/login', 'login', '/logout', 'logout', '/createAccount', 'createAccount',
)
web.config.debug = False
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None})
render = web.template.render('templates/')
class hello:        
    def GET(self):
        if session.user == None:
            return render_template('login.html')
        all_recipes = sqlitedb.getAllRecipes()
        r_photos = sqlitedb.getRecommendedPhotos()
        recommended_photos = []
        for r in r_photos:
            recommended_photos.append(r['Photo'])
        fp = sqlitedb.getFeaturedRecipe()
        featured_recipe_photo = []
        featured_recipe_photo.append(fp['Photo'])
        featured_recipe = sqlitedb.getRecipe(1)
        recommended_recipes = sqlitedb.getRecommendedRecipes(session.user)
        social_feed = sqlitedb.getSocialFeed()
        if social_feed:
            print "printing social feed"
            print social_feed
    	return render_template('curr_time.html', all_recipes = all_recipes, recommended_photos = recommended_photos, featured_recipe_photo = featured_recipe_photo, recommended_recipes = recommended_recipes, user = session.user, social_feed = social_feed, featured_recipe = featured_recipe)

class view:
    def GET(self):
        if session.user == None:
            return render_template('login.html')
        post_params = web.input()
        editAbout = False
        if 'editAboutMe' in post_params:
            editAbout = True
        if 'newAboutMe' in post_params:
            editAbout = False
            sqlitedb.updateAboutMe(userID, post_params['newAboutMe'])
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
        userVotes = {0 : 'na'}
        for review in reviews:
            userVotes[review['ReviewID']] = sqlitedb.userVoted(review['ReviewID'], session.user)
        userHasReviewed = sqlitedb.hasUserReviewed(recipeID, session.user)
        cookbooks = sqlitedb.getCookbooks(session.user)
        userMatchesRecipeAuthor = False
        for result in recipe:
            if session.user == result['UserID']:
                userMatchesRecipeAuthor = True
        return render_template('view_recipe.html', recipe = recipe, recipeID = recipeID, instructions = instructions, ingredients = ingredients, tags = tags, photos = photos, categories = categories, reviews = reviews, cookbooks = cookbooks, currentUser = session.user, userHasReviewed = userHasReviewed, userMatchesRecipeAuthor = userMatchesRecipeAuthor, userVotes = userVotes, editAbout = editAbout)

#added by valerie for reviews
    def POST(self):
        post_params = web.input()
        editAbout = False
        recipeID = post_params['recipeID']
        print post_params
        if 'editAboutMe' in post_params:
            editAbout = True
        if 'newAboutMe' in post_params:
            editAbout = False
            sqlitedb.updateRecipeReview(post_params['reviewID'], post_params['newAboutMe'], int(post_params['stars']))

            #calculate new ratings
            ratings = sqlitedb.getReviews(recipeID)
            counter = 0.0
            total = 0
            for r in ratings:
                total += r['Rating']
                counter += 1.0
            new_rating = total/counter
            new_rating = format(new_rating, '.2f')
            sqlitedb.updateRating(recipeID, new_rating)       
        if 'review' in post_params:
            reviewID = sqlitedb.assignReviewID()
            sqlitedb.addRecipeReview(reviewID, recipeID, session.user, post_params['review'], int(post_params['stars']), 0, 0)

            #need to update overall rating now
            ratings = sqlitedb.getReviews(recipeID)
            counter = 0.0
            total = 0
            for r in ratings:
                total += r['Rating']
                counter += 1.0
            new_rating = total/counter
            new_rating = format(new_rating, '.2f')
            sqlitedb.updateRating(recipeID, new_rating)
        if 'added_cookbookID' in post_params:
                sqlitedb.addCookbookRecipe(recipeID, post_params['added_cookbookID'])
        if 'd' in post_params:
            sqlitedb.deleteReview(post_params['DeleteReview'])
            #need to update overall rating now
            ratings = sqlitedb.getReviews(recipeID)
            counter = 0.0
            total = 0
            for r in ratings:
                total += r['Rating']
                counter += 1.0
            new_rating = total/counter
            new_rating = format(new_rating, '.2f')
            sqlitedb.updateRating(recipeID, new_rating)
        if 'HelpfulReview' in post_params:
            reviewID = post_params['reviewID']
            sqlitedb.addOneThumbsUp(reviewID, session.user)
            sqlitedb.updateVoteReviewStatus(reviewID, session.user, "up")
        if 'UnhelpfulReview' in post_params:
            reviewID = post_params['reviewID']
            sqlitedb.addOneThumbsDown(reviewID, session.user)
            sqlitedb.updateVoteReviewStatus(reviewID, session.user, "down")
        #reload page info
        recipe = sqlitedb.getRecipe(recipeID)
        instructions = sqlitedb.getInstructions(recipeID)
        ingredients = sqlitedb.getIngredients(recipeID)
        tags = sqlitedb.getTags(recipeID)
        photos = sqlitedb.getPhotos(recipeID)
        categories = sqlitedb.getCategories(recipeID)
        reviews = sqlitedb.getReviews(recipeID)
        userVotes = {0 : 'na'}
        for review in reviews:
            userVotes[review['ReviewID']] = sqlitedb.userVoted(review['ReviewID'], session.user)
        print userVotes
        userHasReviewed = sqlitedb.hasUserReviewed(recipeID, session.user)
        cookbooks = sqlitedb.getCookbooks(session.user)
        userMatchesRecipeAuthor = False
        for result in recipe:
            if session.user == result['UserID']:
                userMatchesRecipeAuthor = True
        return render_template('view_recipe.html', recipe = recipe, instructions = instructions, ingredients = ingredients, tags = tags, photos = photos, categories = categories, reviews = reviews, cookbooks = cookbooks, recipeID = recipeID, currentUser = session.user, userHasReviewed = userHasReviewed, userMatchesRecipeAuthor = userMatchesRecipeAuthor, userVotes = userVotes, editAbout = editAbout)
class user:
    def GET(self):
        if session.user == None:
            return render_template('login.html')
        post_params = web.input()
        userID = None
        userRecipes = None
        userAboutMe = None
        userFollowers = None
        userFollowing = None
        userCookbooks = None
        viewingOwnProfile = False
        editAbout = False
        follower = False
        recipes = []
        recipe_photos = []
        currentUser = session.user
        if 'userID' in post_params:
            userID = post_params['userID']
            if userID == session.user:
                viewingOwnProfile = True
        elif session.user:
            userID = session.user
            viewingOwnProfile = True
        else:
            return render_template('login.html')
        if 'editAboutMe' in post_params:
            editAbout = True
        if 'newAboutMe' in post_params:
            editAbout = False
            sqlitedb.updateAboutMe(userID, post_params['newAboutMe'])
        following = sqlitedb.getFollowing(currentUser)
        for r in following:
            print r['UserID']
            if r['UserID'] == userID:
                follower = True
        userRecipes = sqlitedb.getUserRecipes(userID)
        for recipe in userRecipes:
            recipes.append(recipe['RecipeID'])
        if len(recipes) > 0:
            all_photos = sqlitedb.getRecipePhotos(recipes)
            for r in all_photos:
                recipe_photos.append(r['Photo'])
        userAboutMe = sqlitedb.getAboutMe(userID)
        userFollowers = sqlitedb.getFollowers(userID)
        userFollowing = sqlitedb.getFollowing(userID)
        userCookbooks = sqlitedb.getCookbooks(userID)
        if 'unfollowing' in post_params:
            sqlitedb.unfollow(session.user, post_params['unfollowing'])
        print recipe_photos
        return render_template('view_user.html', userID = userID, userRecipes = userRecipes, userAboutMe = userAboutMe, userFollowers = userFollowers, userFollowing = userFollowing, userCookbooks = userCookbooks, viewingOwnProfile = viewingOwnProfile, currentUser = currentUser, editAbout = editAbout, follower = follower, recipe_photos = recipe_photos)
    
    def POST(self):
        post_params = web.input()
        cookbookID = None
        currentUser = session.user
        editAbout = False
        viewingOwnProfile = False
        recipe_photos = []
        recipes = []
        if 'userID' in post_params:
            userID = post_params['userID']
            if userID == session.user:
                viewingOwnProfile = True
        elif session.user:
            userID = session.user
            viewingOwnProfile = True
        else:
            return render_template('login.html')
        if 'editAboutMe' in post_params:
            editAbout = True
        if 'newAboutMe' in post_params:
            editAbout = False
            sqlitedb.updateAboutMe(userID, post_params['newAboutMe'])
        if 'deleteCookbook' in post_params:
            sqlitedb.deleteCookbook(post_params['deleteCookbook'])
        if 'cookbook' in post_params:
            cookbookID = sqlitedb.assignCookbookID()
            sqlitedb.addCookbook(cookbookID, session.user, post_params['cookbook'])
        if 'deleteRecipe' in post_params:
            recipeID = post_params['deleteRecipe']
            sqlitedb.deleteRecipe(recipeID)
            currentUser = session.user
        if 'userID' in post_params:
            userID = post_params['userID']
            userRecipes = sqlitedb.getUserRecipes(userID)
            for recipe in userRecipes:
                recipes.append(recipe['RecipeID'])
            if len(recipes) > 0:
                all_photos = sqlitedb.getRecipePhotos(recipes)
                for r in all_photos:
                    recipe_photos.append(r['Photo'])
            userAboutMe = sqlitedb.getAboutMe(userID)
            userFollowers = sqlitedb.getFollowers(userID)
            userFollowing = sqlitedb.getFollowing(userID)
            userCookbooks = sqlitedb.getCookbooks(userID)
        if 'unfollowing' in post_params:
            sqlitedb.unfollow(session.user, post_params['unfollowing'])
        if 'addFollower' in post_params:
            sqlitedb.addFollower(post_params['addFollower'], session.user)
        return render_template('view_user.html', userID = userID, userRecipes = userRecipes, userAboutMe = userAboutMe, userFollowers = userFollowers, userFollowing = userFollowing, userCookbooks = userCookbooks, viewingOwnProfile=viewingOwnProfile, currentUser = currentUser, editAbout = editAbout, recipe_photos = recipe_photos)

class cookbook:
    # THIS IS NOT COMPLETE YET - 1/31 at 4:28pm
    #Edit: 2/7, Valerie will now try to complete it
    def GET(self):
        if session.user == None:
            return render_template('login.html')
        post_params = web.input()
        cookbookID = None
        cookbookRecipes = None
        cookbookInfo = None
        recipes = []
        all_photos = None
        all_recipes = None 
        cookbookInfo = None
        recipe_photos = []
        if 'cookbookID' in post_params:
            cookbookID = post_params['cookbookID']
            cookbookRecipes = sqlitedb.getCookbooks_recipes(cookbookID)
            for recipe in cookbookRecipes:
                recipes.append(recipe['RecipeID'])
            if len(recipes) > 0:
                all_photos = sqlitedb.getRecipePhotos(recipes)
                all_recipes = sqlitedb.getRecipes(recipes)
                for r in all_photos:
                    recipe_photos.append(r['Photo'])
            cookbookInfo = sqlitedb.getCookbookInfo(cookbookID)
        return render_template('view_cookbook.html', cookbookID = cookbookID, cookbookInfo = cookbookInfo, cookbookRecipes = cookbookRecipes, all_photos = all_photos, all_recipes = all_recipes, currentUser = session.user, recipe_photos = recipe_photos)

    def POST(self):
        if session.user == None:
            return render_template('login.html')
        post_params = web.input()
        cookbookID = None
        cookbookRecipes = None
        cookbookInfo = None
        recipes = []
        recipe_photos = []
        all_photos = None
        all_recipes = None 
        cookbookInfo = None
        recipeID = None
        if 'recipeID' in post_params:
            recipeID = post_params['recipeID']
            cookbookID = post_params['cookbookID']
            sqlitedb.removeRecipeFromCookbook(cookbookID, recipeID)
        if 'cookbookID' in post_params:
            cookbookID = post_params['cookbookID']
            cookbookRecipes = sqlitedb.getCookbooks_recipes(cookbookID)
            for recipe in cookbookRecipes:
                recipes.append(recipe['RecipeID'])
            if len(recipes) > 0:
                all_photos = sqlitedb.getRecipePhotos(recipes)
                all_recipes = sqlitedb.getRecipes(recipes)
                for r in all_photos:
                    recipe_photos.append(r['Photo'])
            cookbookInfo = sqlitedb.getCookbookInfo(cookbookID)
        return render_template('view_cookbook.html', cookbookID = cookbookID, cookbookInfo = cookbookInfo, cookbookRecipes = cookbookRecipes, all_photos = all_photos, all_recipes = all_recipes, currentUser = session.user, recipe_photos = recipe_photos)

class search:
    def GET(self):
        if session.user == None:
            return render_template('login.html')
        return render_template('search_recipes.html')

    def POST(self):
        post_params = web.input()
        recipeID = ""
        userID = post_params['userID']
        recipeName = post_params['recipeName']
        completionTime = post_params['completionTime']
        ingredients = post_params['ingredients'].split()
        categories = []

        if  'categoriesBR' in post_params:
            categories.append("breakfast")
        if 'categoriesLU' in post_params:
            categories.append("lunch")
        if 'categoriesDI' in post_params:
            categories.append("dinner")
        if 'categoriesSA' in post_params:
            categories.append("savory")
        if 'categoriesSW' in post_params:
            categories.append("sweet")
        if 'categoriesVE' in post_params:
            categories.append("vegetarian")
        if 'categoriesGF' in post_params:
            categories.append("gluten free")

        tags = post_params['tags'].split()
        final_search_results = sqlitedb.searchRecipes(recipeID, userID, recipeName, completionTime, ingredients, categories, tags)
        recipe_photos = []
        for result in final_search_results:
            photo = sqlitedb.getPhotos(result['RecipeID'])[0]['Photo']
            print photo
            recipe_photos.append(photo)
        return render_template('search_recipes.html', search_results = final_search_results, recipe_photos = recipe_photos)

class login:
    def GET(self):
        return render_template('login.html')

    def POST(self):
        post_params = web.input()
        userIDInput = post_params['userID']
        passwordInput = post_params['password']
        actualPasswordResult = sqlitedb.getPassword(userIDInput)
        if len(actualPasswordResult) == 0:
            return render_template('login.html', message = "Username " + userIDInput + " does not exist.")
        else:
            actualPassword = actualPasswordResult[0]['Password']
            if passwordInput == actualPassword:
                session.user = userIDInput
                return web.redirect('/hello')
            else:
                return render_template('login.html', message = "Please enter the correct password.")

class logout:
    def GET(self):
        session.kill()
        session.user = None
        return web.redirect('/login')

    def POST(self):
        session.kill()
        session.user = None
        return web.redirect('/login')

class search_users:
    def GET(self):
        if session.user == None:
            return render_template('login.html')
        return render_template('search_users.html')

    def POST(self):
        post_params = web.input()
        userID = post_params['userID']
        search_results = sqlitedb.searchUsers(userID)
        return render_template('search_users.html', search_results = search_results)


#adam's stuff
class upload_page:
    def GET(self):
        if session.user == None:
            return render_template('login.html')
        return render_template('upload_page.html', currentUser = session.user)
    def POST(self):
        recipeID = sqlitedb.assignRecipeID()
        data = web.input()

        sqlitedb.addRecipe(recipeID,
                session.user, #TODO: ADD THE USER ID
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

        sqlitedb.addRecipePhotos(recipeID, data.image)

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

class createAccount:
    def GET(self):
        return render_template('create_account.html')

    def POST(self):
        post_params = web.input()
        username = post_params['userID']
        password = post_params['password']
        confirmPassword = post_params['confirmPassword']
        if username == "":
            return render_template('create_account.html', message = "Please enter a non-empty username")
        if password == "":
            return render_template('create_account.html', message = "Please enter a non-empty password")
        if password != confirmPassword:
            return render_template('create_account.html', message = "Password does not match Confirm Password!")
        usernameExistCheck = sqlitedb.getPassword(username)
        if len(usernameExistCheck) != 0:
            message = "Username '"
            message = message + username
            message = message + "' already exists. Please choose a different username!"
            return render_template('create_account.html', message = message)
        else:
            sqlitedb.addUser(username, password)
            sqlitedb.addAboutMe(username, "Currently no about me.")
            session.user = username
            return web.redirect('/hello')

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