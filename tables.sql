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
Quantity int,
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

Insert into Users values("skaterAdam189", "apple"), ("blubbo", "apple"), ("billy", "apple");
Insert into About_me values("skaterAdam189", "Expert master chef."), ("blubbo", "Here to make new dishes and learn how to cook."), ("billy", "AB. Also I make great recipes! Follow me.");
Insert into Cookbooks values(1, "blubbo", "Blubbo's cookbook");
Insert into Cookbooks_recipes values(1, 1);
Insert into Recipes values(1, "billy", 4, "Broccoli Beef", "The Best Broccoli Beef in town.", 55, 4, "no", 2);
Insert into Instructions values(1, 1, "Get some broccoli."), (1, 2, "Get some beef."), (1,3, "Get some yummy sauce."), (1, 4, "8 dollar donation.");
Insert into Ingredients values(1, "broccoli", 10, "blank"), (1, "beef", 4, "pounds"), (1, "yummy sauce", 2, "oz");
Insert into Tags values(1, "broccoli"), (1, "beef"), (2, "best food ever");
Insert into Photos values (1, "http://162.61.226.249/PicOriginal/P63452612080938_5.jpg");
Insert into Categories values(1, "savory"), (1, "dinner");
Insert into Reviews values(1, "blubbo", "it's good, but the dish could use more beef", 4);
Insert into Followers values("blubbo", "billy");
Insert into Constants values(1, 1);
