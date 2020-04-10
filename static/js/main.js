
setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);



function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
   console.log("NOT SUPPORTED")
  }
}

function showPosition(position) {

  let lat = position.coords.latitude 
  let lon = position.coords.longitude
  console.log("COORDINATES",lat,lon);

 
}

function hey() {

alert("hey")


}