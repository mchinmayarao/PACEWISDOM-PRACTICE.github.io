
const itemsPerPage = 5;
let currentPage = 1;
let jsonData = [];
let maxButtons = 5;

// Fetch JSON data from the file
fetch('movies.json')
    .then(response => response.json())
    .then(data => {
        jsonData = data;
        displayData(currentPage);
        renderPaginationButtons(currentPage);
    })
    .catch(error => console.error('Error fetching JSON:', error));

function displayData(page) {
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const pageData = jsonData.slice(startIndex, endIndex);

    const container = $('.data-container');
    container.empty();
    pageData.forEach(function (movie, i) {
        var sno = i + 1;
        var title = movie.title;
        var imdbRating = movie.imdb.rating;
        var tomatoesRating = movie.tomatoes.viewer.rating;
        var plot = movie.plot;
        
        console.log("sno:", sno);
        console.log("Title:", title);
        console.log("IMDb Rating:", imdbRating);
        console.log("Tomatoes Rating:", tomatoesRating);
        console.log("Plot:", plot);

        var row = $('<tr class="text-center">' +
            '<th id="sno" scope="row">' + sno + '</th>' +
            '<td id="title">' + title + '</td>' +
            '<td id="imdb">' + imdbRating + '</td>' +
            '<td id="rottenTomatoes">' + tomatoesRating + '</td>' +
            '<td id="rottenTomatoes">' + ((tomatoesRating+imdbRating)/2).toFixed(1) + '</td>' +
            '<td id="View">' + plot + '</td>' +
            '</tr>')

        $('tbody').append(row);

    });
}

function renderPaginationButtons() {
    const paginationContainer = $('.pageNum');
    paginationContainer.empty();

    const numPages = Math.ceil(jsonData.length / itemsPerPage);
    let startPage = Math.max(1, currentPage - Math.floor(maxButtons / 2));
    let endPage = Math.min(numPages, startPage + maxButtons - 1);

    startPage = Math.max(1, endPage - maxButtons + 1);

    for (let i = startPage; i <= endPage; i++) {
        const btn = $('<li class="page-item"><button class="page-link pageNumber">' + i + '</button></li>');
        if (i === currentPage) {
            btn.addClass('active');
        }
        btn.find('.pageNumber').click(function() {
            currentPage = i;
            displayData(currentPage);
            renderPaginationButtons();
        });
        paginationContainer.append(btn);
    }
}

$('#previousPage').click(function() {
    if (currentPage > 1) {
        currentPage--;
        displayData(currentPage);
        renderPaginationButtons();
    }
});

$('#nextPage').click(function() {
    const numPages = Math.ceil(jsonData.length / itemsPerPage);
    if (currentPage < numPages) {
        currentPage++;
        displayData(currentPage);
        renderPaginationButtons();
    }
});

