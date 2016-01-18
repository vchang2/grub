#Followers is a stretch goal

drop table if exists Users;
drop table if exists Cookbooks;
drop table if exists Cookbooks_recipes;
drop table if exists Recipes;
drop table if exists Ingredients;
drop table if exists Tags;
drop table if exists Photos;
drop table if exits Categories;
drop table if exists Reviews;
drop table if exists Followers;


create table Users (
UserID text PRIMARY KEY,
Password text);

create table Cookbooks(
CookbookID int PRIMAR KEY,
UserID text REFERENCES Users(UserID),
Cookbook_name text);

create table Cookbooks_recipes(
RecipeID int REFERENCES Recipes(RecipeID),
CookbookID int REFERENCES Cookbooks(CookbookID)
);

#time_completionin minutes!!
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
Quantity int);

create table Tags(
RecipeID int REFERENCES Recipes(RecipeID),
Tags text);

#how do we store photos? as a string text?
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

