Units = [["None", "None"], ["Weight", "pounds", "ounces"], ["Volume", "teaspoons", "tablespoons", "fluid ounces", "cups", "pints", "quarts", "gallons"], ["Small Units", "pinches", "drops"]];

function Ingredient(){
	this.quantity = "";
	this.unit = "none";
	this.ingredient = "";
}

function UploadScript(ingredientsID, instructionsID, imagesID){
	this.ingredientsBody = document.getElementById(ingredientsID);
	this.instructionsBody = document.getElementById(instructionsID);
	this.imagesBody = document.getElementById(imagesID)

	this.ingredients = new Array();	
	this.instructions = new Array();
	this.imagesX = new Array();

	for(var i = 0; i < 3; i++){
		this.ingredients.push(new Ingredient());
		this.instructions.push("");	
	}

	this.imagesX.push("")

	this.renderIngredients();
	this.renderInstructions();
}

UploadScript.prototype.renderIngredients = function(){
	var text = "";

	text += "<input type=\"hidden\" name=\"numIngredients\" value=\"" + this.ingredients.length + "\">";
	text += "<table>";
	text += "<tr><td></td><td>Quantity</td><td>Units</td><td>Ingredient</td></td>";
	
	for(var i = 0; i < this.ingredients.length; i++){
		text += "<tr><td>" + (i + 1) + ". </td>";
		text += "<td><input type=\"text\" id=\"ingredientQuantity" + i + "\" "
		text += "name=\"ingredientQuantity" + i + "\" class=\"quantityTextbox\" value=\"" + this.ingredients[i].quantity + "\"></td>"

		//SELECT BOX

		text += "<td><select id=\"ingredientUnit" + i + "\" "
		text += "name=\"ingredientUnit" + i + "\">";
		
		for(var group = 0; group < Units.length; group++){
			text += "<optgroup label=\"" + Units[group][0] + "\">";
		
			for(var elem = 1; elem < Units[group].length; elem++){
				var selected = "";
		
				if(this.ingredients[i].unit.localeCompare(Units[group][elem]) == 0){
					selected = "selected=\"selected\"";
				}
		
				text += "<option value=\"" + Units[group][elem] + "\"" + selected + ">" + Units[group][elem] + "</option>";
			}
		
			text += "</optgroup>";
		}

		text += "</select></td>";

		//

		text += "<td><input type=\"text\" id=\"ingredientIngredient" + i + "\" "
		text += "name=\"ingredientIngredient" + i + "\" class=\"ingredientTextbox\" value=\"" + this.ingredients[i].ingredient + "\"></td></tr>";
	}
	
	text += "</table>";
	text +="<button type=\"button\" onclick=\"US.addIngredient()\">+ Ingredient</button>";

	this.ingredientsBody.innerHTML = text;
};

UploadScript.prototype.renderInstructions = function(){
	var text = "";

	text += "<input type=\"hidden\" name=\"numInstructions\" value=\"" + this.instructions.length + "\">";
	text += "<table>";
	
	for(var i = 0; i < this.instructions.length; i++){
		text += "<tr><td>" + (i + 1) + ". </td>";
		text += "<td><textarea id=\"instruction" + i + "\" "
		text += "name=\"instruction" + i + "\" rows=\"2\" cols=\"40\">" + this.instructions[i] + "</textarea></td></tr>";
	}
	
	text += "</table>";
	text +="<button type=\"button\" onclick=\"US.addInstruction()\">+ Instruction</button>";

	this.instructionsBody.innerHTML = text;
};

UploadScript.prototype.renderImages = function(){
	var text = "";
	text += "<input type=\"hidden\" name=\"numImages\" value=\"" + this.imagesX.length + "\">";

	for(var i = 0; i < this.imagesX.length; i++){
		text += "<input type=\"text\" id=\"image" + i + "\" "
		text += "name=\"image" + i + "\" value=\"" + this.imagesX[i] + "\"><br/>";
	}

	text +="<button type=\"button\" onclick=\"US.addImage()\">+ Image</button>";

	this.imagesBody.innerHTML = text;
}

UploadScript.prototype.saveIngredients = function(){
	for(var i = 0; i < this.ingredients.length; i++){
		this.ingredients[i].quantity = "" + document.getElementById("ingredientQuantity" + i).value;
		this.ingredients[i].unit = document.getElementById("ingredientUnit" + i).value;
		this.ingredients[i].ingredient = "" + document.getElementById("ingredientIngredient" + i).value;
	}
};

UploadScript.prototype.saveInstructions = function(){
	for(var i = 0; i < this.instructions.length; i++){
		this.instructions[i] = "" + document.getElementById("instruction" + i).value;
	}
};

UploadScript.prototype.saveImages = function(){
	for(var i = 0; i < this.imagesX.length; i++){
		this.imagesX[i] = "" + document.getElementById("image" + i).value;
	}
};

UploadScript.prototype.addIngredient = function(){
	this.saveIngredients();
	this.ingredients.push(new Ingredient);
	this.renderIngredients();
};

UploadScript.prototype.addInstruction = function(){
	this.saveInstructions();
	this.instructions.push("");
	this.renderInstructions();
};

UploadScript.prototype.addImage = function(){
	this.saveImages();
	this.imagesX.push("");
	this.renderImages();
};