var numberOfFriendliers = 10;

//window.onload = createGridItem();

function friendliers(){
  // Function responsible to create an AJAX conenction with the server
  // And retrive the data;
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // Parse the JSON data
      var json_data = JSON.parse(this.responseText);

      createGridItems(10, json_data);
    }
  }

  let requestData = "?n=" + numberOfFriendliers;

  xhttp.open("GET", "/friendliers" + requestData, true);
  xhttp.send();
}

function createGridItems(number, messagesData) {
  // Create a new friendlier
  var divList = [];
  // Create a list of div element which will become a friendlier on the grid;
  for(var i = 0; i < number; i++){
    // Create the element
    divList[i] = document.createElement('div');

    for(let j = 0, paraList = []; j < 3; j++){
      paraList[j] = document.createElement('p');

      paraList[j].setAttribute('id', 'paragrath' + i);

      paraList[j].innerHTML = messagesData[i][j];

      divList[i].appendChild(paraList[j]);
    }
    // Customize with a progressive id;
    divList[i].setAttribute('id', 'friendlier' + i);
    // Append the div into the grid;
    document.getElementById('gridMessages').appendChild(divList[i]);
  }
}
