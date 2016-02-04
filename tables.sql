drop table if exists Users;
drop table if exists About_me;
drop table if exists Cookbooks;
drop table if exists Cookbooks_recipes;
drop table if exists Recipes;
drop table if exists Ingredients;
drop table if exists Tags;
drop table if exists Photos;
drop table if exists Categories;
drop table if exists Reviews;
drop table if exists Followers;
drop table if exists Constants;
drop table if exists Instructions;


create table Users (
UserID varchar(255) PRIMARY KEY,
Password varchar(255));

create table About_me(
UserID varchar(255) REFERENCES Users(UserID),
Description varchar(255));

create table Cookbooks(
CookbookID int PRIMARY KEY,
UserID text REFERENCES Users(UserID),
Cookbook_name text);

create table Cookbooks_recipes(
RecipeID int REFERENCES Recipes(RecipeID),
CookbookID int REFERENCES Cookbooks(CookbookID)
);


create table Recipes(
RecipeID int PRIMARY KEY,
UserID text REFERENCES Users(UserID),
Overall_rating int,
Recipe_name text,
Description text,
Time_completion int,
Num_servings int,
Spicy text,
Difficulty int);

create table Instructions(
RecipeID int REFERENCES Recipes(RecipeID),
Instruction_number int,
Instruction text);

create table Ingredients(
RecipeID int REFERENCES Recipes(RecipeID),
Ingredient text,
Quantity_num int,
Quantity_denom int,
Unit text);

create table Tags(
RecipeID int REFERENCES Recipes(RecipeID),
Tags text);


create table Photos(
RecipeID int REFERENCES Recipes(RecipeID),
Photo text);

create table Categories(
RecipeID int REFERENCES Recipes(RecipeID),
Category text);

create table Reviews(
RecipeID int REFERENCES Recipes(RecipeID),
UserID text REFERENCES Users(UserID),
Review text,
Rating int);

create table Followers(
FollowerID text REFERENCES Users(UserID),
UserID text REFERENCES Users(UserID));

create table Constants(
RecipeID int REFERENCES Recipes(RecipeID),
CookbookID int REFERENCES Cookbooks(CookbookID));

Insert into Users values("Adam189", "apple"), ("blubbo", "apple"), ("billy", "apple");
Insert into About_me values("Adam189", "Expert master chef."), ("blubbo", "Here to make new dishes and learn how to cook."), ("billy", "I make great recipes! Follow me.");
Insert into Cookbooks values(1, "blubbo", "Blubbo's cookbook");
Insert into Cookbooks_recipes values(1, 1), (2, 1);
Insert into Recipes values(1, "billy", 4, "Broccoli Beef", "The Best Broccoli Beef in town.", 55, 4, "no", 2), (2, "Adam189", 4, "Chicken Marsala Ravioli Filling", "Amazing Chicken Ravioli that will warm the heart.", 16, 7, "no", 3),
(3, "billy", 5, "Seared Tofu Banh Mi Sandwiches","A delicate delite enjoyed as a whole-hearted meal.", 25, 3, "yes", 3);
Insert into Instructions values(1, 1, "Get some broccoli."), (1, 2, "Get some beef."), (1,3, "Get some yummy sauce."), (1, 4, "8 dollar donation."), (2, 1, "Brown chicken in 2 tablespoons of olive oil over medium-high heat"), 
(2,2, "Add shallot and garlic."), (2, 3, "Deglaze with Marsala."), (2, 4, "Take pan away from heat source and flambe."), (2, 5, "Return pan to stove, flame will go out in about 1 minute."), (2, 6, "Sprinkle in bread crumbs and 1 tablespoon Parmesan."),
(2, 7, "Drizzle in 1 tablespoon of olive oil to keep moist. Discard bay leaves."), (2, 8, "Pulse together all ingredients in a food processor. Add egg, cream, remaining Parmesan and olive oil."),
(2, 9, "Pulse again. Chill before filling ravioli."), (3, 1, "Make ahead: Place thinly sliced daikon, carrots, cucumbers, and jalapeños in a medium jar with white wine vinegar, rice vinegar, sugar and salt. If the liquids don’t cover the veggies, add about 2 
	tablespoons of water and more vinegar if necessary (the amount you need will depend on the size of your jar). Let chill for at least an hour, or store in the fridge for at least a week."), (3, 2, "Drain tofu, slice it into approx. ½ inch slices. 
	Place on a towel and gently pat dry to remove excess water."), (3, 3, "In a small bowl, whisk together olive oil, tamari, lime, zest, garlic, ginger, and freshly cracked pepper."), (3, 4, "Place tofu in a shallow pan and pour the marinade on top. Flip the 
	tofu so that it coats (if it doesn’t coat fully in your pan, add a bit more tamari until all tofu is coated). Let the tofu marinate for at least 15 minutes."), (3, 5, "Heat a nonstick skillet to medium-high heat. Add a little oil to the pan and place tofu pieces 
	with enough space between each so that they’re not too crowded (you can cook them in batches). Let the tofu cook (without moving it around too much) for a few minutes per side until they’re deeply golden brown and caramelized (almost blackened) around the edges. 
	Remove from heat. Taste a little piece and add more salt & pepper if necessary."), (3, 6, "Assemble sandwiches with mayo, tofu slices, pickled veggies, cilantro and serve with sriracha.");
Insert into Ingredients values(1, "broccoli", 10, 1, "None"), (1, "beef", 4, 1, "pounds"), (1, "yummy sauce", 2, 1,"ounces"), (2, "chicken breast", 8,1, "ounces"), (2, "olive oil", 4, 1,"tablespoons"), (2, "shallot", 1,1, "None"),
(2, "garlic clove", 1,4, "None"), (2, "Marsala wine or chicken broth", 1,2, "cups"), (2, "egg", 1,1, "None"), (2, "thin slices prosciutto", 4,1, "None"), (3, "extra firm tofu", 14, 1, "ounces"), (3, "fresh baguette", 1, 1, "None"), (3, "small daikon sliced into matchsticks", 1, 1, "None"),
(3, "small carrots", 2, 1, "None"), (3, "thinly sliced jalapeño", 1, 2, "None"), (3, "white wine vinegar", 1, 4, "cups"), (3, "salt", 3, 1, "pinches"), (3, "tamari", 2, 1, "tablespoons"), (3, "garlic", 1, 1, "cloves"), (3, "minced ginger", 1, 2, "teaspoons");
Insert into Tags values(1, "broccoli"), (1, "beef"), (2, "best food ever"), (2, "chicken"), (2, "Ravioli"), (2, "Dinner"), (3, "Vietnamese"), (3, "sandwiches");
Insert into Photos values (1, "http://162.61.226.249/PicOriginal/P63452612080938_5.jpg"), 
(2, "http://media.olivegarden.com/images/site/ext/pages/_promotions/specials/flavorfilled-extra-stuffed-pastas/specials_details_flavorfilled_01_1123.jpg"),
(3, "http://www.willowandthyme.com/wp-content/uploads/2015/04/banh-mi-tofu-2fw-150x150.jpg");
Insert into Categories values(1, "savory"), (1, "dinner"), (2, "savory"), (2, "dinner"), (3, "vegetarian"), (2, "snack");
Insert into Reviews values(1, "blubbo", "it's good, but the dish could use more beef", 4), (2, "billy", "I had a wonderful time making this dish. The instructions were well thoughout and put together. It was quite fantastic", 4),
(3, "Adam189", "A really amazing dish. I had a lot of fun making it. Since my wife is vegetarian, it's a great snack for the both of us to enjoy. Easy to make, and delicious to eart!", 5),
(3, "blubbo", "Really great set and stone instructions for a beginner like me. No need for heating anything, and the sandwiches were delicious!!!", 5);
Insert into Followers values("blubbo", "billy"), ("Adam189", "billy");
Insert into Constants values(3, 1);
