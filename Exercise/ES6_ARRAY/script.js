var dataJson = {};

$.getJSON('movies.json', function(data) {
    
    dataJson = data;
    
    var dataLength = Object.entries(data).length;
   // console.log(dataLength);

    var noOfPages = Math.ceil(dataLength/5);

    

    data.forEach(function(movie,i) {
        var sno = i+1;
        var title = movie.title;
        var imdbRating = movie.imdb.rating;
        var tomatoesRating = movie.tomatoes.viewer.rating;
        var plot = movie.plot;
        
        console.log("sno:", sno);
        console.log("Title:", title);
        console.log("IMDb Rating:", imdbRating);
        console.log("Tomatoes Rating:", tomatoesRating);
        console.log("Plot:", plot);
    
        var row = $( '<tr class="text-center">' +
        '<th id="sno" scope="row">' + sno + '</th>'+
        '<td id="title">' + title + '</td>' +
        '<td id="imdb">' + imdbRating + '</td>' +
        '<td id="rottenTomatoes">' +tomatoesRating + '</td>' +
        '<td id="View">' +plot + '</td>' +
        '</tr>' )
    
        $('tbody').append(row);
    
      });

})

function addPageNumber(num){

    for(var i =0; i<num; i++){
        var btn = $('<li class="page-item"><button class="page-link btn btn-link pageNumber" id="btn'+(i+1) + '">' + (i+1) + '</button></li>');
        $('.pageNum').append(btn);
    }
}