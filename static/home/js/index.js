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

function OpenPortfolioModal(name,description,id) {
    document.getElementById('portfolioModalTitle').innerText = name;
    document.getElementById('portfolioModalDescription').innerText = description;
    $.ajax({
        url: "/api/product/" + id,
        beforeSend: function () {
            document.getElementById("portfolioModalProduct").innerHTML = ""
        },
        success: function (result) {
            let result_string = "";
            result.data.forEach(s=>{
                result_string += '<figure class="col-lg-3 col-md-4 col-sm-6 portfolio-item">' +
                    '<a href=https://www.newpearl.co.nz/index.php/product/'+ s.code+' data-size="1600x1067">' +
                    '<img style="height: 224px;width: 224px" alt="picture" src='+ s.image +' class="img-fluid" alt="picture" />' +
                    '</a>' +
                    '<p style="color:#000;">'+ s.code +'</p>'+
                    '</figure>'
            })
            document.getElementById('portfolioModalProduct').innerHTML = result_string
        }
    })
}


