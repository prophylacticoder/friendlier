var positionCounter = 0;

//window.onload = createGridItem();

function friendliers(){
  // Function responsible to create an AJAX conenction with the server
  // And retrive the data;
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // Parse the JSON data
      var json_data = JSON.parse(this.responseText);

      createGridItems(json_data.length, json_data);
    }
  }

  let requestData = "?position=" + (positionCounter + 1).toString();

  xhttp.open("GET", "/friendliers" + requestData, true);
  xhttp.send();
}

function createGridItems(number, messagesData) {
  // Create a new friendlier
  var divList = [];
  // Create a list of the paragraph classes
  var paragraghClasses = ['firstParagraph', 'secondParagraph', 'thirdParagraph', ];

  // Create a list of div element which will become a friendlier on the grid;
  for(var i = 0; i < number; i++){
    // Create the element
    divList[i] = document.createElement('div');

    for(let j = 0, paraList = []; j < 3; j++){
      paraList[j] = document.createElement('p');

      paraList[j].setAttribute('id', 'paragrath' + i);

      // Add a class to the currently paragraph
      paraList[j].className = paragraghClasses[j];

      paraList[j].innerHTML = messagesData[i][j];

      divList[i].appendChild(paraList[j]);
    }

    divList[i].setAttribute('class', 'friendliersClass');
    // Append the div into the grid;
    document.getElementById('gridMessages').appendChild(divList[i]);
  }
  positionCounter += number;
}
