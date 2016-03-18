function SearchScript(displayID, IMG_HEIGHT, IMG_WIDTH, prefix = ""){
	if(IMG_HEIGHT <= 0){
		IMG_HEIGHT = 300;
	}
	if(IMG_WIDTH <= 0){
		IMG_WIDTH = 400;
	}
	var padding = 20;
	var INFO_PADDING = 20;
	var INFO_DOWN = IMG_HEIGHT - 60;
	var COL_2_WIDTH = 100;
	var STAR_SIZE = 20;
	var GRADIENT_DEFAULT_HEIGHT = 100;
	var GRADIENT_EXTENDED_HEIGHT = 200;
	var INFO_SHIFT = 30;
	displayDiv = document.getElementById(displayID);
	var numPhotos = document.getElementById(prefix + "numPhotos").value;
	if(numPhotos == 0){
		return;
	}
	var displayDivStyle = window.getComputedStyle(displayDiv);
	var width = displayDivStyle.width;
	var originalOffset = findPos(displayDiv);
	var offset = findPos(displayDiv);
	var numLines = 1;
	for(var i = 0; i < numPhotos; i++){
		var image = document.getElementById(prefix + "recipePhoto" + i);
		var linkArea = document.getElementById(prefix + "linkArea" + i);
		var gradient = document.getElementById(prefix + "gradient" + i);
		if(image == null){
			
			//image
			image = document.createElement("img");
			image.id = prefix + "recipePhoto" + i;
			image.src = document.getElementById(prefix + "photo" + i).value;
			image.style.height = IMG_HEIGHT + "px";
			image.style.position = "fixed";
			displayDiv.appendChild(image);
			//var width = image.clientWidth;
			var width = image.getBoundingClientRect().right - image.getBoundingClientRect().left;
			if (width > IMG_WIDTH){
				var widthToRemove = image.clientWidth - IMG_WIDTH;
				image.style.clip = "rect(0px " + IMG_WIDTH + "px " + IMG_HEIGHT +  "px 0px)";
				width = IMG_WIDTH;
			}
			//gradient
			gradient = document.createElement("img");
			gradient.id = prefix + "gradient" + i;
			gradient.src = "../static/images/gradient1.png";
			gradient.style.height = GRADIENT_DEFAULT_HEIGHT + "px";
			gradient.style.width = width;
			gradient.style.position = "fixed";
			gradient.name = "" + GRADIENT_DEFAULT_HEIGHT;
			displayDiv.appendChild(gradient);
			//link
			var link = document.createElement("a");
			link.href = document.getElementById(prefix + "url" + i).value;
			linkArea = document.createElement("div");
			linkArea.id = prefix + "linkArea" + i;
			linkArea.style.height = IMG_HEIGHT + "px";
			linkArea.style.width = width + "px";
			linkArea.style.position = "fixed";
			linkArea.style.zIndex = "100";
			linkArea.onmouseover = function(event){
				var num = event.target.id.slice(-1);
				var mouse = document.getElementById(prefix + "mouseOver" + num);
				mouse.value = "Y";
				var grad = document.getElementById(prefix + "gradient" + num);
				grad.style.height = GRADIENT_EXTENDED_HEIGHT + "px";
				var user2 = document.getElementById(prefix + "userName" + num);
				user2.style.color = "white";
				user2.style.textShadow = "2px 2px 2px #000000";
				
				var time2 = document.getElementById(prefix + "recipeTime" + num);
				time2.style.color = "white";
				time2.style.textShadow = "2px 2px 2px #000000";
				SearchScript(displayID, IMG_HEIGHT, IMG_WIDTH, prefix);
				/*
				var num = event.target.id.slice(-1);
				var grad = document.getElementById(prefix + "gradient" + num);
				grad.style.height = GRADIENT_EXTENDED_HEIGHT + "px";
				var imgBox = document.getElementById(prefix + "recipePhoto" + num).getBoundingClientRect();
				grad.style.top = (imgBox.bottom + GRADIENT_EXTENDED_HEIGHT) + "px";
				//verticallyShift(grad, (GRADIENT_DEFAULT_HEIGHT - GRADIENT_EXTENDED_HEIGHT));
				//verticallyShift(document.getElementById(prefix + "recipeName" + num), -1*INFO_SHIFT);
				//for(var j = 0; j < 5; j++){
				//	verticallyShift(document.getElementById(prefix + "star" + num + '_' + j), -1*INFO_SHIFT);
				//}
				var user2 = document.getElementById(prefix + "userName" + num);
				user2.style.color = "white";
				user2.style.textShadow = "2px 2px 2px #000000";
				var time2 = document.getElementById(prefix + "recipeTime" + num);
				time2.style.color = "white";
				time2.style.textShadow = "2px 2px 2px #000000";
				*/
			};
			linkArea.onmouseout = function(event){
				var num = event.target.id.slice(-1);
				var mouse = document.getElementById(prefix + "mouseOver" + num);
				mouse.value = "N";
				
				var grad = document.getElementById(prefix + "gradient" + num);
				grad.style.height = GRADIENT_DEFAULT_HEIGHT + "px";
				
				var user2 = document.getElementById(prefix + "userName" + num);
				user2.style.color = "transparent";
				user2.style.textShadow = "";
				
				var time2 = document.getElementById(prefix + "recipeTime" + num);
				time2.style.color = "transparent";
				time2.style.textShadow = "";
				SearchScript(displayID, IMG_HEIGHT, IMG_WIDTH, prefix);
				/*
				var num = event.target.id.slice(-1);
				var grad = document.getElementById(prefix + "gradient" + num);
				grad.style.height = GRADIENT_DEFAULT_HEIGHT + "px";
				verticallyShift(grad, (GRADIENT_EXTENDED_HEIGHT - GRADIENT_DEFAULT_HEIGHT));
				verticallyShift(document.getElementById(prefix + "recipeName" + num), INFO_SHIFT);
				for(var j = 0; j < 5; j++){
					verticallyShift(document.getElementById(prefix + "star" + num + '_' + j), INFO_SHIFT);
				}
				var user2 = document.getElementById(prefix + "userName" + num);
				user2.style.color = "transparent";
				user2.style.textShadow = "";
				var time2 = document.getElementById(prefix + "recipeTime" + num);
				time2.style.color = "transparent";
				time2.style.textShadow = "";
				*/
			}
			link.appendChild(linkArea);
			displayDiv.appendChild(link);
			//mouseover div
			var mouse = document.createElement("input");
			mouse.id = prefix + "mouseOver" + i;
			mouse.type = "hidden";
			mouse.value = "N";
			displayDiv.appendChild(mouse);
			//name
			var name = document.createElement("p");
			name.id = prefix + "recipeName" + i;
			name.innerHTML = document.getElementById(prefix + "name" + i).value;
			name.style.textAlign = "left";
			name.style.color = "white";
			name.style.textShadow = "2px 2px 2px #000000";
			name.style.position = "fixed";
			name.style.fontWeight = "bold";
			name.style.fontSize = "20px";
			name.style.whiteSpace = "nowrap";
    		name.style.width = "" + (width - 3*padding - 5*STAR_SIZE) + "px";
    		name.style.overflow = "hidden";
    		name.style.textOverflow = "ellipsis";
			displayDiv.appendChild(name);
			//stars
			var rating = parseFloat(document.getElementById(prefix + "rating" + i).value);
			for(var j = 0; j < 5; j++){
				var star = document.createElement("img");
				star.id = prefix + "star" + i + '_' + j;
				var picVal = rating - j;
				picVal = Math.min(Math.max(picVal, 0), 1);
				picVal *= 10;
				picVal = Math.round(picVal);
				star.src = "../static/images/Stars/Star" + picVal + ".png";
				star.style.width = STAR_SIZE + "px";
				star.style.height = STAR_SIZE + "px";
				star.style.position = "fixed";
				displayDiv.appendChild(star);
			}
			//user
			var user = document.createElement("p");
			user.id = prefix + "userName" + i;
			user.innerHTML = document.getElementById(prefix + "user" + i).value;
			user.style.textAlign = "left";
			user.style.color = "transparent";
			user.style.textShadow = "";
			user.style.position = "fixed";
			user.style.fontSize = "20px";
			user.style.whiteSpace = "nowrap";
    		user.style.width = "" + (width - 3*padding - 5*STAR_SIZE) + "px";
    		user.style.overflow = "hidden";
    		user.style.textOverflow = "ellipsis";
			displayDiv.appendChild(user);
			//time
			var time = document.createElement("p");
			time.id = prefix + "recipeTime" + i;
			time.innerHTML = document.getElementById(prefix + "time" + i).value + " min";
			time.style.color = "transparent";
			time.style.textShadow = "";
			time.style.position = "fixed";
			time.style.fontSize = "20px";
			time.style.whiteSpace = "nowrap";
    		time.style.width = "" + (5*STAR_SIZE) + "px";
    		time.style.overflow = "hidden";
    		time.style.textOverflow = "ellipsis";
			displayDiv.appendChild(time);
		}
		
		var width = image.getBoundingClientRect().right - image.getBoundingClientRect().left;
		deltaX = width;
		if (width > IMG_WIDTH){
			deltaX = IMG_WIDTH;
		}
		deltaX += padding;
		if (i != 0 && offset['X'] + deltaX > window.innerWidth - originalOffset['X'] - padding){
			offset['X'] = originalOffset['X'];
			offset['Y'] += IMG_HEIGHT + padding;
			numLines += 1;
		}
		var imageLeft = offset['X'] - document.body.scrollLeft;
		var imageTop = offset['Y'] - document.body.scrollTop;
		var infoLeft = imageLeft + INFO_PADDING;
		var infoTop = imageTop + INFO_DOWN;
		image.style.left = "" + imageLeft + "px";
		image.style.top = "" + imageTop + "px";
		linkArea.style.left = "" + imageLeft + "px";
		linkArea.style.top = "" + imageTop + "px";
		var mouseOver = (document.getElementById(prefix + "mouseOver" + i).value == "Y");
		var gradientDelta = GRADIENT_DEFAULT_HEIGHT;
		var infoTopDelta = 0;
		if(mouseOver){
			gradientDelta = GRADIENT_EXTENDED_HEIGHT
			infoTopDelta = INFO_SHIFT;
		}
		gradient.style.left = "" + imageLeft + "px";
		gradient.style.top = "" + (imageTop + IMG_HEIGHT - gradientDelta) + "px";
		width = image.getBoundingClientRect().right - image.getBoundingClientRect().left;
		//gradient.style.width = width + "px";
		//image.style.boxShadow="10px 20px 30px blue";//"0px 7px 5px -5px #666666 inset";
		//Title of recipe
		var name = document.getElementById(prefix + "recipeName" + i);
		name.style.left = "" + infoLeft + "px";
		name.style.top = "" + (infoTop - infoTopDelta) + "px";
		var user = document.getElementById(prefix + "userName" + i);
		user.style.left = "" + infoLeft + "px";
		user.style.top = "" + infoTop + "px";
		var time = document.getElementById(prefix + "recipeTime" + i);
		time.style.left = "" + (imageLeft + deltaX - time.clientWidth - padding) + "px";
		time.style.top = "" + infoTop + "px";
		//Stars
		var imageWidth = image.clientWidth;
		if(imageWidth > IMG_WIDTH){
			imageWidth = IMG_WIDTH
		}
		for(var j = 0; j < 5; j++){
			var star = document.getElementById(prefix + "star" + i + '_' + j)
			star.style.top = (infoTop + 20 - infoTopDelta) + "px";
			star.style.left = "" + (imageLeft + imageWidth - INFO_PADDING - ((5-j) * STAR_SIZE)) + "px";
			//star.style.left = "" + (imageLeft + imageWidth - INFO_PADDING - (STAR_SIZE)) + "px";
			//star.style.left = "" + (imageLeft + INFO_PADDING + (j * STAR_SIZE)) + "px";
		}
		offset['X'] += deltaX;
	}
	spaceDiv = document.getElementById(prefix + 'space');
	spaceDiv.innerHTML = "";
	for(var i = 0; i < numLines; i++){
		//TODO: 5/6? Why?
		spaceDiv.innerHTML += '<div style=\"font-size:' + (IMG_HEIGHT + padding)*5/6 + 'px\"><br/></div>';
	}
}
function findPos(obj){
	var curleft = 0;
	var curtop = 0;
	if (obj.offsetParent) {
		do {
			curleft += obj.offsetLeft;
			curtop += obj.offsetTop;
		} while (obj = obj.offsetParent);
		
		return {X:curleft,Y:curtop};
	}
}
function verticallyShift(obj, value){
	obj.style.top = (parseInt(obj.style.top.substring(0, 3)) + value) + "px";
}