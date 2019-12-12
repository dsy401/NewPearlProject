function paginationHandler(i) {
    var search = window.location.search;
    var final;
    if (search==="" || search === "?"){
        final = "/store/tiles_categories?page="+i.toString()
    }else{
        var page_position = search.indexOf('page=');
        if (page_position === -1){
            final = search+"&page=" + i
        }else{
            var substring = search.slice(page_position);
            var and_position = substring.indexOf("&");
            if (and_position === -1){
                final = '/product/tiles_categories' + search.slice(0,page_position) + "page="+ i.toString()
            }else{
                final = '/product/tiles_categories' + search.slice(0,page_position) + 'page=' + i.toString() + search.slice(page_position+and_position,)
            }
        }
    }

    window.location = final
}


function getTileCategorySearchCheckBox() {
    var search = window.location.search
    var tile_category_id_arr = [];

    while (true){
        let tile_category_id_position = search.indexOf("tile_category_id=")
        if (tile_category_id_position == -1) break;

        let and_position = search.indexOf("&")
        if (and_position==-1){
            tile_category_id_arr.push(search.slice(tile_category_id_position+17))
            break;
        }else{
            tile_category_id_arr.push(search.slice(tile_category_id_position+17,and_position))
            search = search.slice(0,tile_category_id_position) + search.slice(and_position+1)
        }

    }
    return tile_category_id_arr

}

function AddToCartHandler(){
    document.cookie = "a=1"
}



window.onload = function () {
    getTileCategorySearchCheckBox().forEach(s=>{
        document.getElementById(s).setAttribute("checked","true")
    })
}

