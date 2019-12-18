function initMap() {
  // The location of Uluru
  var uluru = {lat: -36.7329607, lng: 174.7137635};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}
