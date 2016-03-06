function SearchScript(displayID){
	var IMG_HEIGHT = 30;
	var IMG_WIDTH = 400;
	var padding = 20;

	displayDiv = document.getElementById(displayID);
	var numPhotos = document.getElementById("numPhotos").value;
	if(numPhotos == 0){
		return;
	}

	var displayDivStyle = window.getComputedStyle(displayDiv);
	var width = displayDivStyle.width;
	//var left = displayDivStyle.offsetLeft;

	//window.alert(left);

	var originalOffset = findPos(displayDiv);
	var offset = findPos(displayDiv);
	//window.alert(offset['X']);

	var numLines = 1;

	for(var i = 0; i < numPhotos; i++){
		var image = document.getElementById("recipePhoto" + i);
		if(image == null){
			image = document.createElement("img");
			image.id = "recipePhoto" + i;
			image.src = document.getElementById("photo" + i).value;


			image.style.height = IMG_HEIGHT + "px";
			image.style.position = "fixed";
			//image.style.clip = "rect(0px 75px 75px 0px)";
			displayDiv.appendChild(image);
			var width = image.clientWidth;

			if (image.clientWidth > IMG_WIDTH){
				//window.alert(image.clientWidth);
				var widthToRemove = image.clientWidth - IMG_WIDTH;
				//image.style.clip = "rect(0px " + IMG_WIDTH + "px " + IMG_HEIGHT +  "px 0px)";
				image.style.clip = "rect(0px " + IMG_WIDTH + "px " + IMG_HEIGHT +  "px 0px)";
				//image.style.clip = "0px 0px 0px 0px"
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

		image.style.left = "" + (offset['X'] - document.body.scrollLeft) + "px";
		image.style.top = "" + (offset['Y'] - document.body.scrollTop) + "px";
		offset['X'] += deltaX;

		//image.style.boxShadow = "10px 20px 30px blue inset";
		//displayDiv.appendChild(image);
	}

	for(var i = 0; i < numLines; i++){
		displayDiv.innerHTML += '<div style=\"font-size:' + (IMG_HEIGHT + padding) + 'px\"><br/></div>';
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