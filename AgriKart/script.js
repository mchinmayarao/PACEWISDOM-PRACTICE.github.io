$(document).ready(function () {
    // Fetch and display products
    $.getJSON('JSON/seeds.json', function (data) {
        // Iterate through each product in the JSON data
        $.each(data, function (index, product) {
            // Bootstrap card for each product
            var card = $('<div class="col-md-4">' +
                '<div class="card">' +
                '<img src="' + product.imageSrc + '" class="card-img-top" alt="' + product.name + '" style="padding: 10px;">' +
                '<div class="card-body">' +
                '<h5 class="card-title">' + product.name + '</h5>' +
                '<p class="card-text">Price: ₹ ' + product.price.toFixed(2) + '</p>' +
                '<p class="card-text">Rating: <span class="rating">' + product.rating + '</span></p>' +
                '<p class="card-text">Seller: ' + product.seller + '</p>' +
                '<button class="btn btn-success btn-sm" onclick="addToCart(\'' + product.name + '\')">Add to Cart</button>' +
                '</div>' +
                '</div>' +
                '</div>');

            // Append the card to the row
            $('.row').append(card);
        });
    });
});

// Function for adding to the cart
function addToCart(productName) {
    
    alert('Added ' + productName + ' to the cart!');
}
