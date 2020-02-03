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
            document.getElementById("productLoadingSpinner").style.display = "inline-block"
        },
        success: function (result) {
            console.log(result)
             document.getElementById("productLoadingSpinner").style.display = "none"
            let result_string = "";
            result.data.forEach(s=>{
                result_string += '<figure class="col-lg-3 col-md-4 col-sm-6 portfolio-item">' +
                    "<a href='Javascript:void(0)' onclick='ToProductDetail("+ JSON.stringify(s)+")' data-size='1600x1067'>" +
                    '<img style="height: 224px;width: 224px" alt="picture" src='+ s.image[0] +' class="img-fluid" alt="picture" />' +
                    '</a>' +
                    '<p style="color:#000;">'+ s.code +'</p>'+
                    '</figure>'
            })
            document.getElementById('portfolioModalProduct').innerHTML = result_string
        }
    })
}

function SearchByProductCode() {
    let text = document.getElementById('ProductSearchCode').value;
    document.getElementById("portfolioModalDescription").innerHTML = ""
    if (text.length <=0){
        document.getElementById('portfolioModalTitle').innerText = 'Search Result - ALL';
        $.ajax({
            url: '/api/product',
            beforeSend: function () {
                document.getElementById("portfolioModalProduct").innerText = ""
                document.getElementById("productLoadingSpinner").style.display = "inline-block"
            },
            success: function (result) {
                document.getElementById("productLoadingSpinner").style.display = "none"
                let result_string = ""
                result.data.forEach(s=>{
                    result_string += '<figure class="col-lg-3 col-md-4 col-sm-6 portfolio-item">' +
                        "<a href='Javascript:void(0)' onclick='ToProductDetail("+ JSON.stringify(s)+")' data-size='1600x1067'>" +
                        '<img style="height: 224px;width: 224px" alt="picture" src='+ s.image[0] +' class="img-fluid" alt="picture" />' +
                        '</a>' +
                        '<p style="color:#000;">'+ s.code +'</p>'+
                        '</figure>'
                })
                document.getElementById('portfolioModalProduct').innerHTML = result_string
            }
        })
        return;
    }
    document.getElementById('portfolioModalTitle').innerText = 'Search Result - ' + text;
    $.ajax({
        url: '/api/product/search/' + text,
        beforeSend: function () {
            document.getElementById("portfolioModalProduct").innerText = ""
            document.getElementById("productLoadingSpinner").style.display = "inline-block"
        },
        success: function (result) {
            document.getElementById("productLoadingSpinner").style.display = "none"
            let result_string = ""
            result.data.forEach(s=>{
                result_string += '<figure class="col-lg-3 col-md-4 col-sm-6 portfolio-item">' +
                    "<a href='Javascript:void(0)' onclick='ToProductDetail("+ JSON.stringify(s)+")' data-size='1600x1067'>" +
                    '<img style="height: 224px;width: 224px" alt="picture" src='+ s.image[0] +' class="img-fluid" alt="picture" />' +
                    '</a>' +
                    '<p style="color:#000;">'+ s.code +'</p>'+
                    '</figure>'
            })
            document.getElementById('portfolioModalProduct').innerHTML = result_string
        }
    });


}


function ToProductDetail(obj) {
    const langauge = document.getElementById("language").innerText
    const url = langauge==="English"? '/product/'+obj._id.$oid: '/product/cn/'+obj._id.$oid
    window.open(url)
}



function ModalClose() {
    setTimeout(function () {
        document.getElementById("portfolioproduct").style.opacity = "1";
        document.getElementById("portfolioproduct").style.display = "inline-block";
    },200)
}



function OpenQRCodeModal(name,image) {

    const langauge = document.getElementById("language").innerText
    const description = langauge=="English"?'Add ' + name + ' as a friend':'添加' + name + '为好友'
    document.getElementById('qrcode').innerHTML =
        '<p class="item-intro text-muted">' +
        description +
        '</p>' +
        '<img class="img-fluid" src="'+ image +'"/>'
}


var IWindowWidth = window.innerWidth;
var swiper;
    if (IWindowWidth < 576){
        swiper = new Swiper('.swiper-container', {
            slidesPerView: 1,
            spaceBetween: 30,
            autoplay: {
                delay: 2000,f
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
        });
    }else if (IWindowWidth <767 ) {
        swiper = new Swiper('.swiper-container', {
            slidesPerView: 1,
            spaceBetween: 15,
            autoplay: {
                delay: 2000,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
        });
    }else if (IWindowWidth < 1210){
        swiper = new Swiper('.swiper-container', {
            slidesPerView: 2,
            spaceBetween: 15,
            autoplay: {
                delay: 2000,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
        });
    }
    else{
        swiper = new Swiper('.swiper-container', {
            slidesPerView: 3,
            spaceBetween: 15,
            autoplay: {
                delay: 2000,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
        });
    }


$( window ).resize(function() {
    var WindowWidth = window.innerWidth;
    if (WindowWidth < 576){
        swiper.params.slidesPerView = 1
    }else if (WindowWidth <767){
        swiper.params.slidesPerView = 1
    }else if (WindowWidth < 1210){
        swiper.params.slidesPerView = 2
    }
    else{
        swiper.params.slidesPerView = 3
    }
});



$('.swiper-slide').on('mouseover', function() {
  swiper.autoplay.stop();
});

$('.swiper-slide').on('mouseout', function() {
  swiper.autoplay.start();
});