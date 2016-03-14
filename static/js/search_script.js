function SearchScript(displayID){
	var IMG_HEIGHT = 300;
	var IMG_WIDTH = 400;
	var padding = 20;

	var INFO_PADDING = 20;
	var INFO_DOWN = 240;
	var COL_2_WIDTH = 100;
	var STAR_SIZE = 20;

	displayDiv = document.getElementById(displayID);
	var numPhotos = document.getElementById("numPhotos").value;
	if(numPhotos == 0){
		return;
	}

	var displayDivStyle = window.getComputedStyle(displayDiv);
	var width = displayDivStyle.width;

	var originalOffset = findPos(displayDiv);
	var offset = findPos(displayDiv);

	var numLines = 1;

	for(var i = 0; i < numPhotos; i++){
		var image = document.getElementById("recipePhoto" + i);
		var linkArea = document.getElementById("linkArea" + i);
		if(image == null){
			
			//image
			image = document.createElement("img");
			image.id = "recipePhoto" + i;
			image.src = document.getElementById("photo" + i).value;
			image.style.height = IMG_HEIGHT + "px";
			image.style.position = "fixed";
			displayDiv.appendChild(image);
			var width = image.clientWidth;

			if (width > IMG_WIDTH){
				var widthToRemove = image.clientWidth - IMG_WIDTH;
				image.style.clip = "rect(0px " + IMG_WIDTH + "px " + IMG_HEIGHT +  "px 0px)";
				width = IMG_WIDTH;
			}

			//link
			var link = document.createElement("a");
			link.href = document.getElementById("url" + i).value;
			linkArea = document.createElement("div");
			linkArea.id = "linkArea" + i;
			linkArea.style.height = IMG_HEIGHT + "px";
			linkArea.style.width = width + "px";
			linkArea.style.position = "fixed";
			linkArea.style.zIndex = "100";
			linkArea.onmouseover = function(){

			};
			linkArea.onmouseout = function(){

			}
			link.appendChild(linkArea);
			displayDiv.appendChild(link);

			//name
			var name = document.createElement("p");
			name.id = "recipeName" + i;
			name.innerHTML = document.getElementById("name" + i).value;
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
			//window.alert("before");
			var rating = parseFloat(document.getElementById("rating" + i));
			//window.alert("after");
			for(var j = 0; j < 5; j++){
				var star = document.createElement("img");
				star.id = "star" + i + '_' + j;
				star.src = "../static/images/Stars/Star10.png";
				if(rating < j){
					star.src = "../static/images/Stars/Star0.png";
				}
				star.style.width = STAR_SIZE + "px";
				star.style.height = STAR_SIZE + "px";
				star.style.position = "fixed";
				displayDiv.appendChild(star);
			}
		}
		
		var width = image.clientWidth;

		deltaX = width;
		if (width > IMG_WIDTH){
			deltaX = IMG_WIDTH;
		}

		deltaX += padding;

		if (offset['X'] + deltaX > window.innerWidth - originalOffset['X'] - padding){
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

		//image.style.boxShadow="10px 20px 30px blue";//"0px 7px 5px -5px #666666 inset";

		//Title of recipe
		var name = document.getElementById("recipeName" + i);
		name.style.left = "" + infoLeft + "px";
		name.style.top = "" + infoTop + "px";

		//Stars
		var imageWidth = image.clientWidth;
		if(imageWidth > IMG_WIDTH){
			imageWidth = IMG_WIDTH
		}
		for(var j = 0; j < 5; j++){
			var star = document.getElementById("star" + i + '_' + j)
			star.style.top = (infoTop + 20) + "px";
			star.style.left = "" + (imageLeft + imageWidth - INFO_PADDING - ((5-j) * STAR_SIZE)) + "px";
			//star.style.left = "" + (imageLeft + imageWidth - INFO_PADDING - (STAR_SIZE)) + "px";
			//star.style.left = "" + (imageLeft + INFO_PADDING + (j * STAR_SIZE)) + "px";
		}


		offset['X'] += deltaX;

	}

	spaceDiv = document.getElementById('space');
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