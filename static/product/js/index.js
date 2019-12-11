function paginationHandler(i) {
    var search = window.location.search;
    var final;
    if (search==="" || search === "?"){
        final = "/product/tiles_categories?page="+i.toString()
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


function tileCategorySearch() {
    var search = window.location.search;
    var result;
    var lowest_bound = document.getElementById("lowest-bound").value;
    var highest_bound = document.getElementById('highest-bound').value;

    window.location = "/product/tiles_categories?lowest_bound=" + lowest_bound + "&highest_bound=" + highest_bound
}