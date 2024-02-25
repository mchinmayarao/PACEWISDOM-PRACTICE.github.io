

var currentPageCategory = getPageCategory();
// console.log(currentPageCategory);

switch (currentPageCategory){
    case "fertilizers":
        $.getJSON('../JSON/products.json', function (data) {
            // console.log(data[0]["fertilizers"]);
            displayProducts(data[0]["fertilizers"]);
        });
        break;
    case "seeds":
        $.getJSON('../JSON/products.json', function (data) {
            // console.log(data[1]["seeds"]);
            displayProducts(data[1]["seeds"]);
        });
        break;
    case "toolsandequipments":
        $.getJSON('../JSON/products.json', function (data) {
            // console.log(data[2]["toolsAndEquipments"]);
            displayProducts(data[2]["toolsAndEquipments"]);
        });
        break;
    case "allproducts":
        $.getJSON('../JSON/products.json', function (data) {
            displayProducts(data[0]["fertilizers"]);
            displayProducts(data[1]["seeds"]);
            displayProducts(data[2]["toolsAndEquipments"]);
        });
        break;
        
    
}



function addToCart(productName) {
    alert('Added ' + productName + ' to the cart!');
}


function getPageCategory() {
    var pathArray = window.location.pathname.split('/');
    var currentPage = pathArray[pathArray.length - 1].split('.')[0];
    return currentPage.toLowerCase();
}

// Function to display products dynamically
export function displayProducts(data) {
    $.each(data, function (index, product) {
        // Bootstrap card for each product
        var card = $('<div class="col-md-4">' +
            '<div class="card id = "' + product.id + '">' +
            '<img src="../' + product.imageSrc + '" class="card-img-top" alt="' + product.name + '" style="padding: 10px;">' +
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
        $('#productRow').append(card);
    });
}


// function search(){
//     var searchItem = document.getElementById("search-form").value.toLowerCase();
//     console.log(searchItem);
// }


(function () {
    function search() {
        var txt = document.getElementById('search-form').value;
        console.log(txt);
    }

    document.getElementById('search-btn').addEventListener('click', search, true);
})();

// $(document).ready(function () {
    
//     var currentPageCategory = getPageCategory();

//     $.getJSON('../JSON/'  + currentPageCategory + '.json', function (data) {
//         displayProducts(data);
//     });
// });


// function addToCart(productName) {
//     console.log(productName);
//     alert('Added ' + productName + ' to the cart!');
// }


// function getPageCategory() {
//     var pathArray = window.location.pathname.split('/');
//     var currentPage = pathArray[pathArray.length - 1].split('.')[0];
//     return currentPage.toLowerCase();
// }

// // Function to display products dynamically
// function displayProducts(data) {
//     $.each(data, function (index, product) {
//         // Bootstrap card for each product
//         var card = $('<div class="col-md-4">' +
//             '<div class="card">' +
//             '<img src="../' + product.imageSrc + '" class="card-img-top" alt="' + product.name + '" style="padding: 10px;">' +
//             '<div class="card-body">' +
//             '<h5 class="card-title">' + product.name + '</h5>' +
//             '<p class="card-text">Price: ₹ ' + product.price.toFixed(2) + '</p>' +
//             '<p class="card-text">Rating: <span class="rating">' + product.rating + '</span></p>' +
//             '<p class="card-text">Seller: ' + product.seller + '</p>' +
//             '<button class="btn btn-success btn-sm" onclick="addToCart(\'' + product.name + '\')">Add to Cart</button>' +
//             '</div>' +
//             '</div>' +
//             '</div>');

//         // Append the card to the row
//         $('#productRow').append(card);
//     });
// }