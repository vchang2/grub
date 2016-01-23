drop table if exists Users;
drop table if exists Cookbooks;
drop table if exists Cookbooks_recipes;
drop table if exists Recipes;
drop table if exists Ingredients;
drop table if exists Tags;
drop table if exists Photos;
drop table if exists Categories;
drop table if exists Reviews;
drop table if exists Followers;


create table Users (
UserID varchar(255) PRIMARY KEY,
Password varchar(255));

create table Cookbooks(
CookbookID int PRIMAR KEY,
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
Instructions text,
Time_completion int,
Num_servings int,
Spicy text,
Difficulty int);

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

Insert into Users values("skaterAdam189", "apple"), ("blubbo", "apple"), ("billy", "apple");

Insert into Cookbooks values(1, "blubbo", "Blubbo's cookbook");
Insert into Cookbooks_recipes values(1, 1);
Insert into Recipes values(1, "billy", 4, "Broccoli Beef", "The Best Broccoli Beef in town.", "1. Get some broccoli. 2. Get some beef. 3. Get some yummy sauce. 4. 8 dollar donation.", 55, 4, "no", 2);
Insert into Ingredients values(1, "broccoli", 10, "blank"), (1, "beef", 4, "pounds"), (1, "yummy sauce", 2, "oz");
Insert into Tags values(1, "broccoli"), (1, "beef"), (2, "best food ever");
Insert into Photos values (1, "http://162.61.226.249/PicOriginal/P63452612080938_5.jpg");
Insert into Categories values(1, "savory"), (1, "dinner");
Insert into Reviews values(1, "blubbo", "it's good, but the dish could use more beef", 4);
Insert into Followers values("blubbo", "billy");
