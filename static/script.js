var numberOfFriendliers = 10;

function friendliers(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("logo").innerHTML = this.responseText;
    }
  };
  let requestData = "?n=" + numberOfFriendliers;
  xhttp.open("GET", "/friendliers" + requestData, true);
  xhttp.send();
}
