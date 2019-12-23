function initMap() {
  var location = {lat: -36.7329607, lng: 174.7137635};

  var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 15 ,
      center: new google.maps.LatLng(location.lat,location.lng),
  });


  var marker = new google.maps.Marker({
      position: location,
      map: map,
      title:"Thriving Building",
      label:{
          color: "black",
          text: "Unit 2, 59 Corinthian Drive, Albany",
          fontWeight: "bold"
      }
  });
}
