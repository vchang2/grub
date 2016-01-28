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

def getFollowers(username):
    query_string = 'select * from Followers where UserID = $userID'
    results = query(query_string, {'userID': username})
    return results

def getFollowing(username):
    query_string = 'select * from Followers where FollowerID = $userID'
    results = query(query_string, {'userID': username})
    return results

def assignRecipeID():
    query_string = 'select * from LastRecipeID'
    result = query(query_string)
    recipeID = result + 1
    query_string = 'insert into LastRecipeID values ($recipeID)'
    db.query(query_string, {'recipeID':recipeID})
    return recipeID

# Added by Ryan on 1/27 at 9:12pm or later
def getAllRecipes():
    query_string = 'select * from Recipes'
    result = query(query_string)
    return result

def getAllPhotos():
    query_string = 'select * from Photos'
    results = query(query_string)
    return results

