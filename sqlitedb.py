import web

db = web.database(dbn='sqlite',
        db='database.db' #TODO: add your SQLite database filename
    )

######################BEGIN HELPER METHODS######################

# Enforce foreign key constraints
# WARNING: DO NOT REMOVE THIS!
def enforceForeignKey():
    db.query('PRAGMA foreign_keys = ON')

# initiates a transaction on the database
def transaction():
    return db.transaction()
# Sample usage (in auctionbase.py):
#
# t = sqlitedb.transaction()
# try:
#     sqlitedb.query('[FIRST QUERY STATEMENT]')
#     sqlitedb.query('[SECOND QUERY STATEMENT]')
# except Exception as e:
#     t.rollback()
#     print str(e)
# else:
#     t.commit()
#
# check out http://webpy.org/cookbook/transactions for examples

# wrapper method around web.py's db.query method
# check out http://webpy.org/cookbook/query for more info
def query(query_string, vars = {}):
    return list(db.query(query_string, vars))

def getUsers():
    query_string = 'select * from Users'
    results = query(query_string)
    return results

# returns a single item specified by the Item's ID in the database
# Note: if the `result' list is empty (i.e. there are no items for a
# a given ID), this will throw an Exception!
def getItemById(item_id):
    # TODO: rewrite this method to catch the Exception in case `result' is empty
    query_string = 'select * from Items where item_ID = $itemID'
    result = query(query_string, {'itemID': item_id})
    return result[0]

#####################END HELPER METHODS#####################

#TODO: additional methods to interact with your database,
# e.g. to update the current time
def addUser(username, password):
    query_string = 'insert into Users values ($username, $password)'
    db.query(query_string, {'username': username, 'password': password})

def getCookbooks(username):
    query_string = 'select * from Cookbooks where UserID = $userID'
    results = query(query_string, {'userID' : username})
    return results

def getCookbookInfo(CookbookID):
    query_string = 'select * from Cookbooks where CookbookID = $cookbookID'
    results = query(query_string, {'cookbookID': CookbookID})
    return results

def getCookbooks_recipes(cookbookID):
    query_string = 'select * from Cookbooks_recipes where CookbookID = cookbookID'
    results = query(query_string, {'cookbookID': cookbookID})
    return results

def getRecipe(recipeID):
    query_string = 'select * from Recipes where RecipeID = $recipeID'
    result = query(query_string, {'recipeID':recipeID})
    return result

def getIngredients(recipeID):
    query_string = 'select * from Ingredients where RecipeID = $recipeID'
    results = query(query_string, {'recipeID':recipeID})
    return results

def getInstructions(recipeID):
    query_string = 'select * from Instructions where RecipeID = $recipeID ORDER BY Instruction_number'
    results = query(query_string, {'recipeID':recipeID})
    return results

def getTags(recipeID):
    query_string = 'select * from Tags where RecipeID = $recipeID'
    results = query(query_string, {'recipeID': recipeID})
    return results

def getPhotos(recipeID):
    query_string = 'select * from Photos where RecipeID = $recipeID'
    results = query(query_string, {'recipeID': recipeID})
    return results

def getCategories(recipeID):
    query_string = 'select * from Categories where RecipeID = $recipeID'
    results = query(query_string, {'recipeID': recipeID})
    return results

def getReviews(recipeID):
    query_string = 'select * from Reviews where RecipeID = $recipeID'
    results = query(query_string, {'recipeID': recipeID})
    return results

#People who is following the user
def getFollowers(username):
    query_string = 'select * from Followers where UserID = $userID'
    results = query(query_string, {'userID': username})
    return results

#These are the people the user is following
def getFollowing(username):
    query_string = 'select * from Followers where FollowerID = $userID'
    results = query(query_string, {'userID': username})
    return results


#not sure if correct
def assignRecipeID():
    query_string = 'select * from Constants'
    result = query(query_string)
    replace = 0
    for r in result:
        replace = r['RecipeID']
    recipeID = replace + 1
    query_string = 'update Constants set RecipeID = $recipeID where RecipeID = $replace'
    db.query(query_string, {'recipeID':recipeID, 'replace':replace })
    return recipeID

def assignCookbookID():
    query_string = 'select * from Constants'
    result = query(query_string)
    replace = 0
    for r in result:
        replace = r['CookbookID']
    CookbookID = replace + 1
    query_string = 'update LastRecipeID set CookbookID = $cookbookID where CookbookID = $replace'
    db.query(query_string, {'cookbookID':CookbookID, 'replace':replace})
    return CookbookID

# Added by Ryan on 1/27 at 9:12pm or later
def getAllRecipes():
    query_string = 'select * from Recipes'
    result = query(query_string)
    return result

def getAllPhotos():
    query_string = 'select * from Photos'
    results = query(query_string)
    return results

#added by Valerie on 1/31, a lot of the inserting Recipe data into database queries are here
def getPassword(username):
    query_string = 'select Password from Recipes where UserID = $username'
    results = query(query_string, {'username': username})
    return results

#for overall rating, put in 0 if it hasn't been rated yet
def addRecipe(RecipeID, UserID, Overall_rating, Recipe_name, Description, Time_completion, Num_servings, Spicy, Difficulty):
    query_string = 'insert into Recipes values ($recipeID, $userID, $overall_rating, $recipe_name, $description, $time_completion, $num_servings, $spicy, $difficulty)'
    db.query(query_string, {'recipeID': RecipeID, 'userID':UserID, 'overall_rating':Overall_rating, 'recipe_name':Recipe_name, 'description':Description, 'time_completion':Time_completion, 'num_servings':Num_servings, 'spicy':Spicy, 'difficulty':Difficulty})

def addRecipeCategories(RecipeID, Category):
    query_string = 'insert into Categories values($recipeID, $category)'
    db.query(query_string, {'recipeID':RecipeID, 'category':Category})

def addRecipeTags(RecipeID, Tag):
    query_string = 'insert into Tags values($recipeID, $tag)'
    db.query(query_string, {'recipeID':RecipeID, 'tag': Tag})

def addRecipePhotos(RecipeID, Photo_url):
    query_string = 'insert into Photos values($recipeID, $photo_url)'
    db.query(query_string, {'recipeID':RecipeID, 'photo_url':Photo_url})

def addRecipeInstruction(RecipeID, Instruction_number, Instruction):
    query_string = 'insert into Instructions values($recipeID, $instruction_number, $instruction)'
    db.query(query_string, {'recipeID':RecipeID, 'instruction_number':Instruction_number, 'instruction':Instruction})

def addRecipeIngredients(RecipeID, Ingredient, Quantity_num, Quantity_denom, Unit):
    query_string = 'insert into Ingredients values($recipeID, $ingredient, $quantity_num, $quantity_denom, $unit)'
    db.query(query_string, {'recipeID':RecipeID, 'ingredient':Ingredient, 'quantity_num':Quantity_num, 'quantity_denom':Quantity_denom, 'unit':Unit})

def getAboutMe(username):
    query_string = 'select * from About_me where UserID = $username'
    results = query(query_string, {'username':username})
    return results

def getUserRecipes(username):
    query_string = 'select * from Recipes where UserID = $username'
    results = query(query_string, {'username':username})
    return results

def addRecipeReview(RecipeID, UserID, Review, Rating):
    query_string = 'insert into Reviews values($recipeID, $userID, $review, $rating)'
    db.query(query_string, {'recipeID':RecipeID, 'userID':UserID, 'review':Review, 'rating':Rating})

def addFollower(FollwerID, FolloweeID):
    query_string = 'insert into Followers values($followerID, $followeeID)'
    db.query(query_string, {'followerID':FollwerID, 'followeeID':FolloweeID})

def addCookbook(CookbookID, UserID, Name):
    query_string = 'insert into Cookbooks values($cookbookID, $userID, $name)'
    db.query(query_string, {'cookbookID':CookbookID, 'userID':UserID, 'name':Name})

def addCookbookRecipe(RecipeID, CookbookID):
    query_string = 'insert into Cookbooks_recipes values($recipeID, $cookbookID)'
    db.query(query_string, {'recipeID':RecipeID, 'cookbookID':CookbookID})

def addAboutMe(UserID, Description):
    query_string = 'insert into About_me values($userID, $description)'
    db.query(query_string, {'userID':UserID, 'description':Description})

def updateAboutMe(UserID, Description):
    query_string = 'update About_me set Description = $description where UserID = $userID'
    db.query(query_string, {'description':Description, 'userID':UserID})

# Search Recipe Queries (Ryan, Wednesday 2/3)
def searchRecipes(recipeID, userID, recipeName, completionTime, ingredients, categories, tags):
    query_string = 'select * from Recipes'
    if recipeID != "":
        query_string += ' where RecipeID = $recipeID'
    else:
        query_string += ' where RecipeID = RecipeID'
    if userID != "":
        query_string += ' and UserID = $userID'
    if recipeName != "":
        recipeInput = recipeName
        recipeName = '%'
        recipeName += recipeInput
        recipeName += '%'
        query_string += ' and Recipe_name LIKE $recipeName'
    if completionTime == '1':
        query_string += ' and Time_completion <= 30'
    elif completionTime == '2':
        query_string += ' and Time_completion >= 30 and Time_completion <= 60'
    elif completionTime == '3':
        query_string += ' and Time_completion >= 60 and Time_completion <= 90'
    elif completionTime == '4':
        query_string += ' and Time_completion >= 90'
    if ingredients != "":
        for ingredient in ingredients:
            ingredientForQuery = '%'
            ingredientForQuery += ingredient
            ingredientForQuery += '%'
            query_string += ' and RecipeID in (SELECT RecipeID from Ingredients where Ingredient LIKE "'
            query_string += ingredientForQuery
            query_string += '")'
    if categories != "":
        firstCategory = True
        for category in categories:
            if firstCategory:
                query_string += ' and (RecipeID in (SELECT RecipeID from Categories where Category = "';
            else:
                query_string += ' or RecipeID in (SELECT RecipeID from Categories where Category = "';
            query_string += category
            query_string += '")'
            firstCategory = False
        if firstCategory == False:
            query_string += ')'
    if tags != "":
        firstTag = True
        for tag in tags:
            if firstTag:
                query_string += ' and (RecipeID in (SELECT RecipeID from Tags where Tags = "';
            else:
                query_string += ' or RecipeID in (SELECT RecipeID from Tags where Tags = "';
            query_string += tag
            query_string += '")'
            firstTag = False
        if firstTag == False:
            query_string += ')'
    results = query(query_string, {'recipeID':recipeID, 'userID':userID, 'recipeName':recipeName})
    return results

#Added by Valerie
def getRecipeByCategory(Category):
    query_string = 'select * from Categories where Category = $category'
    results = query(query_string, {'category' : Category})
    return results

def getRecipeByTag(Tag):
    query_string = 'select * from Tags where Tags = $tag'
    results = query(query_string, {'tag' : Tag})
    return results

def updateRating(recipeID, new_rating):
    query_string = 'update Recipes set Overall_rating = $overall_rating where RecipeID = $recipeID'
    db.query(query_string, {'overall_rating':new_rating, 'recipeID':recipeID})

def searchUsers(userID):
    userID = '%' + userID + '%' 
    query_string = 'select * from Users where UserID LIKE $userID'
    results = query(query_string, {'userID': userID})
    return results
