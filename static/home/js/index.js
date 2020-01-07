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
             document.getElementById("productLoadingSpinner").style.display = "none"
            let result_string = "";
            result.data.forEach(s=>{
                result_string += '<figure class="col-lg-3 col-md-4 col-sm-6 portfolio-item">' +
                    "<a href='Javascript:void(0)' onclick='ToProductDetail("+ JSON.stringify(s)+")' data-size='1600x1067'>" +
                    '<img style="height: 224px;width: 224px" alt="picture" src='+ s.image +' class="img-fluid" alt="picture" />' +
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
                        '<img style="height: 224px;width: 224px" alt="picture" src='+ s.image +' class="img-fluid" alt="picture" />' +
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
                    '<img style="height: 224px;width: 224px" alt="picture" src='+ s.image +' class="img-fluid" alt="picture" />' +
                    '</a>' +
                    '<p style="color:#000;">'+ s.code +'</p>'+
                    '</figure>'
            })
            document.getElementById('portfolioModalProduct').innerHTML = result_string
        }
    });


}



function ToProductDetail(product) {
    const langauge = document.getElementById("language").innerText
    let table = "";
    if (langauge == "English"){
        table =
        "<table class='table table-bordered text-center'>" +
            "<thead>" +
                "<tr>" +
                    "<th scope='row'>"+ "Color" +"</th>"+
                    "<td>" + product.color +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "Environment" +"</th>"+
                    "<td>" + product.environment +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "Finish" +"</th>"+
                    "<td>" + product.finish +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "Material" +"</th>"+
                    "<td>" + product.material +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "Price" +"</th>"+
                    "<td>" + product.price +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "Shape" +"</th>"+
                    "<td>" + product.shape +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "Size" +"</th>"+
                    "<td>" + product.size +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "Type" +"</th>"+
                    "<td>" + product.type +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "unit" +"</th>"+
                    "<td>" + product.unit +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "Style" +"</th>"+
                    "<td>" + product.style +"</td>"+
                "</tr>"+

            "</thead>" +
        "</table>"
    }else{
        table =
        "<table class='table table-bordered text-center'>" +
            "<thead>" +
                "<tr>" +
                    "<th scope='row'>"+ "颜色" +"</th>"+
                    "<td>" + product.color_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "适用场景" +"</th>"+
                    "<td>" + product.environment_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "完成度" +"</th>"+
                    "<td>" + product.finish_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "材料" +"</th>"+
                    "<td>" + product.material_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "价格" +"</th>"+
                    "<td>" + product.price_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "形状" +"</th>"+
                    "<td>" + product.shape_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "大小" +"</th>"+
                    "<td>" + product.size_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "类别" +"</th>"+
                    "<td>" + product.type_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "单位" +"</th>"+
                    "<td>" + product.unit_cn +"</td>"+
                "</tr>"+
                "<tr>" +
                    "<th scope='row'>"+ "风格" +"</th>"+
                    "<td>" + product.style_cn +"</td>"+
                "</tr>"+

            "</thead>" +
        "</table>"
    }
    const back_word = langauge=="English"?" Back":" 返回"
    console.log(back_word)
    // 操作
    document.getElementById("portfolioproductdetail").innerHTML =
        "<div class='row text-center'>"+
        "<div class='col-lg-12 mx-auto'>" +
        "<div class='modal-body'>" +
        "<h2 class='text-uppercase'>"+ product.code +"</h2>"+
        "<p class='item-intro text-muted'>"+ document.getElementById('portfolioModalTitle').innerText +"</p>" +
        "</div>"+
        "</div>"+
        "<div class='row'>" +
        "<div class='col-12 col-sm-12 col-md-6 col-lg-6 col-xl-6'>" +
        "<img style='max-height: 524px' class='img-fluid text-center' alt='product' src='"+ product.image+"'/>"+
        "</div>" +
        "<div class='col-12 col-sm-12 col-md-6 col-lg-6 col-xl-6'>" +
            table +
        "</div>"+
        "</div>"+
        "</div>"+
            '<button onclick="ModalBack()" class="btn btn-primary text-center" type="button"><i class="fas fa-arrow-left"></i>'+ back_word +'</button>'
    //end
    document.getElementById('back-button').style.opacity = '1'
    document.getElementById("portfolioproduct").style.opacity = "0"
    document.getElementById("portfolioproductdetail").style.display = "inline-block"
    setTimeout(function () {
        document.getElementById("portfolioproduct").style.display = "none"
        document.getElementById("portfolioproductdetail").style.opacity = "1"

    },600)
}


function ModalClose() {
    document.getElementById("portfolioproductdetail").style.display = 'none'
     document.getElementById('back-button').style.opacity = '0'
    setTimeout(function () {
        document.getElementById("portfolioproduct").style.opacity = "1";
        document.getElementById("portfolioproduct").style.display = "inline-block";
        document.getElementById("portfolioproductdetail").style.opacity = "0"
    },200)
}

function ModalBack() {
    document.getElementById('back-button').style.opacity = '0'
    document.getElementById("portfolioproductdetail").style.opacity = "0"
    setTimeout(function () {
        document.getElementById("portfolioproductdetail").style.display = 'none'
        document.getElementById("portfolioproduct").style.display = "inline-block";
        document.getElementById("portfolioproduct").style.opacity = "1";
    },600)
}