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
Overall_rating real,
Recipe_name text,
Description text,
Time_completion int,
Num_servings int,
Spicy text,
Difficulty text);

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
Insert into Cookbooks_recipes values(1, 1), (2, 1), (3, 1), (6, 1);
Insert into Recipes values(1, "billy", 4.00, "Broccoli Beef", "The Best Broccoli Beef in town.", 55, 4, "no", "Intermediate Cook"), (2, "Adam189", 4.00, "Chicken Marsala Ravioli Filling", "Amazing Chicken Ravioli that will warm the heart.", 16, 7, "no", "Master Chef"),
(3, "billy", 5.00, "Seared Tofu Banh Mi Sandwiches","A delicate delite enjoyed as a whole-hearted meal.", 25, 3, "yes", "Master Chef"),
(4, "blubbo", 3.50, "Green Quesadillas", "In this frigid weather, nothing sounds better to me than soups and sandwiches. But 
	if you’re like me and you keep tortillas on hand more regularly than bread – quesadillas are the perfect little soup or salad accompaniment.", 12, 1, "yes", "Kitchen Novice"),
(5, "Adam189", 0, "Lemon Pesto Spaghetti Squash", "As pasta, it’s kind of mushy. As a roasted vegetable that happens to form into little strands, it’s so delicious.", 20, 1, "no", "Master Chef"),
(6, "billy", 5.00, "Bread Stuffing", "A dish that brings the kids home and the family together.", 45, 10, "no", "Master Chef");
Insert into Instructions values(1, 1, "Get some broccoli."), (1, 2, "Get some beef."), (1,3, "Get some yummy sauce."), (1, 4, "8 dollar donation."), (2, 1, "Brown chicken in 2 tablespoons of olive oil over medium-high heat"), 
(2,2, "Add shallot and garlic."), (2, 3, "Deglaze with Marsala."), (2, 4, "Take pan away from heat source and flambe."), (2, 5, "Return pan to stove, flame will go out in about 1 minute."), (2, 6, "Sprinkle in bread crumbs and 1 tablespoon Parmesan."),
(2, 7, "Drizzle in 1 tablespoon of olive oil to keep moist. Discard bay leaves."), (2, 8, "Pulse together all ingredients in a food processor. Add egg, cream, remaining Parmesan and olive oil."),
(2, 9, "Pulse again. Chill before filling ravioli."), (3, 1, "Make ahead: Place thinly sliced daikon, carrots, cucumbers, and jalapeños in a medium jar with white wine vinegar, rice vinegar, sugar and salt. If the liquids don’t cover the veggies, add about 2 
	tablespoons of water and more vinegar if necessary (the amount you need will depend on the size of your jar). Let chill for at least an hour, or store in the fridge for at least a week."), (3, 2, "Drain tofu, slice it into approx. ½ inch slices. 
	Place on a towel and gently pat dry to remove excess water."), (3, 3, "In a small bowl, whisk together olive oil, tamari, lime, zest, garlic, ginger, and freshly cracked pepper."), (3, 4, "Place tofu in a shallow pan and pour the marinade on top. Flip the 
	tofu so that it coats (if it doesn’t coat fully in your pan, add a bit more tamari until all tofu is coated). Let the tofu marinate for at least 15 minutes."), (3, 5, "Heat a nonstick skillet to medium-high heat. Add a little oil to the pan and place tofu pieces 
	with enough space between each so that they’re not too crowded (you can cook them in batches). Let the tofu cook (without moving it around too much) for a few minutes per side until they’re deeply golden brown and caramelized (almost blackened) around the edges. 
	Remove from heat. Taste a little piece and add more salt & pepper if necessary."), (3, 6, "Assemble sandwiches with mayo, tofu slices, pickled veggies, cilantro and serve with sriracha."),
	(4, 1, "Make your pickled onions: place ingredients in a small jar, shake it and chill in the fridge for at least 20 minutes (they'll keep for at least a few weeks)."), (4, 2, "Pile cheese, greens, jalapeños, cilantro, and a few pickled onions onto tortillas. 
		Heat a skillet over medium heat. Fold the tortillas in half and cook quesadillas for a few minutes on each side, until the cheese is melted."), (4, 3, "Enjoy as-is or with toppings of your choice."),
	(5, 1, "Preheat the oven to 400°F and line two baking sheets with parchment paper."), (5, 2, "Slice the spaghetti squash in half lengthwise and scrape out the seeds. Drizzle each half with olive oil, sprinkle with salt and pepper, and place on a baking sheet cut side up. 
		Roast until fork-tender, about 1 hour. Drizzle the cauliflower with olive oil, sprinkle with salt and pepper, and place on the second baking sheet. Roast for about 25 minutes or until golden brown around the edges."), 
	(5, 3, "Meanwhile, make the pesto and set aside."), (5, 4, "Place the baby spinach in a large bowl. Use a fork to scrape the spaghetti squash into strands. Add the lemon juice and season to taste with salt and pepper (you can do this right in the spaghetti squash halves). 
		Add the spaghetti squash to the bowl and gently toss, so that the heat from the squash lightly wilts the spinach leaves."), (5, 5, "Add the roasted cauliflower, pine nuts, parsley, and a dollop of the pesto."),
	(5,6, "Optional step: toss it all together so that the pesto coats all of the vegetables."),
	(5, 7, "Serve with lemon wedges, extra pesto, and parmesan, if desired."),
	(6, 1, "Melt butter in 4-quart Dutch oven over medium-high heat. Cook celery and onion in butter 6 to 8 minutes, stirring occasionally, until tender. Remove Dutch oven from the heat."),
	(6, 2, "Gently toss celery mixture and remaining ingredients, using spoon, until bread cubes are evenly coated."),
	(6, 3, "Use to stuff one 10- to 12-pound turkey. Or to bake stuffing separately, grease 3-quart casserole or rectangular baking dish, 13x9x2 inches. Place stuffing in casserole or baking dish. Cover with lid or aluminum foil and bake at 325°F for 30 minutes; uncover and bake 15 minutes longer.");
Insert into Ingredients values(1, "broccoli", 10, 1, "None"), (1, "beef", 4, 1, "pounds"), (1, "yummy sauce", 2, 1,"ounces"), (2, "chicken breast", 8,1, "ounces"), (2, "olive oil", 4, 1,"tablespoons"), (2, "shallot", 1,1, "None"),
(2, "garlic clove", 1,4, "None"), (2, "Marsala wine or chicken broth", 1,2, "cups"), (2, "egg", 1,1, "None"), (2, "thin slices prosciutto", 4,1, "None"), (3, "extra firm tofu", 14, 1, "ounces"), (3, "fresh baguette", 1, 1, "None"), (3, "small daikon sliced into matchsticks", 1, 1, "None"),
(3, "small carrots", 2, 1, "None"), (3, "thinly sliced jalapeño", 1, 2, "None"), (3, "white wine vinegar", 1, 4, "cups"), (3, "salt", 3, 1, "pinches"), (3, "tamari", 2, 1, "tablespoons"), (3, "garlic", 1, 1, "cloves"), (3, "minced ginger", 1, 2, "teaspoons"), (4, "tortillas", 4, 1, "None"),
(4, "shredded cheese", 2, 1, "ounces"), (4, "sliced jalapeño", 1, 2, "None"), (4, "cilantro sprigs", 1, 1, "None"), (4, "shallot",1, 1, "None"), (4, "white wine", 8, 1, "ounces"), (4, "avacado", 2, 1, "None"), (5, "extra virgin olive oil", 8, 1, "ounces"),
(5, "spaghetti squash", 1, 1, "None"), (5, "baby spinach", 2, 1, "cups"), (5, "cauliflower florets", 2, 1, "cups"), (5, "lemon", 1, 2, "None"), (5, "pine nuts", 2, 1, "tablespoons"), (5, "chopped fresh herbs", 1, 4, "cups"),
(6, "butter", 3, 4, "cups"), (6, "chopped celery sticks",2, 1, "None"), (6, "onion", 1, 2, "cups"), (6, "soft bread cubes", 9, 1, "cups"), (6, "fresh thyme leaves", 3, 4, "cups"), (6, "salt", 2, 1, "teaspoons"), (6, "pepper", 1, 4, "teaspoons");
Insert into Tags values(1, "broccoli"), (1, "beef"), (2, "best food ever"), (2, "chicken"), (2, "Ravioli"), (2, "Dinner"), (3, "Vietnamese"), (3, "sandwiches"), (4, "mexican"), (4, "quesadillas"), (5, "squash"), (6, "stuffing"), (6, "bread"), (6, "family");
Insert into Photos values (1, "http://162.61.226.249/PicOriginal/P63452612080938_5.jpg"), 
(2, "http://media.olivegarden.com/images/site/ext/pages/_promotions/specials/flavorfilled-extra-stuffed-pastas/specials_details_flavorfilled_01_1123.jpg"),
(3, "http://www.willowandthyme.com/wp-content/uploads/2015/04/banh-mi-tofu-2fw-871x1024.jpg"), (4, "http://dev.ctevisions.com/bluelemon/wp-content/uploads/2013/10/kids-green-ques1.jpg"), 
(5, "http://lh3.googleusercontent.com/_6BFsRu-4WQr7Z0nCZHHQAMpHuWPLmWZSI-KkgSU9UoIQ2fZ51Aw0O_erwSPBOSVzvzMl2lkSC1W0GvOSs25=s480-c-e365"),
(6, "http://images.edge-generalmills.com/5a1831d5-6c87-4c93-b3b5-465f2367c608.jpg");
Insert into Categories values(1, "savory"), (1, "dinner"), (2, "savory"), (2, "dinner"), (3, "vegetarian"), (3, "snack"), (4, "gluten-free"), (5, "snack"), (6, "savory"), (6, "dinner"), (6, "lunch");
Insert into Reviews values(1, "blubbo", "it's good, but the dish could use more beef", 4), (2, "billy", "I had a wonderful time making this dish. The instructions were well thoughout and put together. It was quite fantastic", 4),
(3, "Adam189", "A really amazing dish. I had a lot of fun making it. Since my wife is vegetarian, it's a great snack for the both of us to enjoy. Easy to make, and delicious to eart!", 5),
(3, "blubbo", "Really great set and stone instructions for a beginner like me. No need for heating anything, and the sandwiches were delicious!!!", 5), (4, "Adam189", "Blubbo is one of our newer members to the community. This is 
	a really great start, but would have liked to see more thorough instructions to carry out this dish. But an incredible idea", 2), (4, "billy", "I've had quesadillas: chicken, cheese, chicken and cheese, mushroom, you name it. But never green!
	It tastes a lot better than expected!", 5), (6, "blubbo", "Amazing! This tasted so great, and really tasted like the bread stuffing my grandma used to make. It's delicious, thanks so much!", 5);
Insert into Followers values("blubbo", "billy"), ("Adam189", "billy");
Insert into Constants values(6, 1);
