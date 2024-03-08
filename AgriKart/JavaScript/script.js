
function getPageCategory() {
    var pathArray = window.location.pathname.split('/');
    var currentPage = pathArray[pathArray.length - 1].split('.')[0];
    return currentPage;
}

var currentPageCategory = getPageCategory();
console.log(currentPageCategory);

function getPageCategoryIndex() {

    switch (currentPageCategory) {
        case "fertilizers":
            return 0;
        case "seeds":
            return 1;
        case "toolsAndEquipments":
            return 2;
        case "allProducts":
            break;
    }

}

var currentPageCategoryIndex = getPageCategoryIndex();
// console.log(currentPageCategoryIndex);

switch (currentPageCategory) {
    case "fertilizers":
        $.getJSON('../JSON/products.json', function (data) {
            // console.log(key);
            console.log(data);
            displayProducts(data[0]["fertilizers"]);
        });
        break;
    case "seeds":
        $.getJSON('../JSON/products.json', function (data) {
            // console.log(data[1]["seeds"]);
            displayProducts(data[1]["seeds"]);
        });
        break;
    case "toolsAndEquipments":
        $.getJSON('../JSON/products.json', function (data) {
            // console.log(data[2]["toolsAndEquipments"]);
            displayProducts(data[2]["toolsAndEquipments"]);
        });
        break;
    case "allProducts":
        $.getJSON('../JSON/products.json', function (data) {
            displayProducts(data[0]["fertilizers"]);
            displayProducts(data[1]["seeds"]);
            displayProducts(data[2]["toolsAndEquipments"]);
        });
        break;
    case "cart":
        var isLoggedIn = sessionStorage.getItem("isLoggedIn");
        if (isLoggedIn == 'false') {
            window.location.href = '../html/index.html';
        }
        break;

    case "checkout":
        var isLoggedIn = sessionStorage.getItem("isLoggedIn");
        if (isLoggedIn == 'false') {
            window.location.href = '../html/index.html';
        }
        break;
    case "account":
        var isLoggedIn = sessionStorage.getItem("isLoggedIn");
        if (isLoggedIn == 'false') {
            window.location.href = '../html/index.html';
        }
}






function displayProducts(data) {
    $.each(data, function (index, product) {
        // Check if discount is available
        var discountedPrice = (product.discount / 100) * product.price;
        // Bootstrap card for each product
        var card = $('<div class="col-md-4">' +
            '<div class="card" id="' + product.id + '" style="margin-bottom: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">' +
            '<img src="../' + product.imageSrc + '" class="card-img-top img-fluid" alt="' + product.name + '" style="padding: 10px; border-top-left-radius: 10px; border-top-right-radius: 10px;">' +
            '<div class="card-body" style="padding: 10px;">' +
            '<h5 class="card-title">' + product.name + '</h5>' +
            '<p class="card-text"><strong>Price:</strong> ₹ <span class="original-price">' + product.price.toFixed(2) + '</span></p>' +
            '<p class="card-text"><strong>Discounted Price:</strong> ₹ <span class="discounted-price">' + discountedPrice.toFixed(2) + '</span></p>' +
            '<p class="card-text"><strong>Rating:</strong> <span class="badge bg-info">' + product.rating + '</span></p>' +
            '<p class="card-text"><strong>Seller:</strong> ' + product.seller + '</p>' +
            '<div class="text-center ">' +
            '<button class="btn btn-success addToCart" style="margin-bottom:10px;margin-top:10px" onclick="addToCart(\'' + product.name + '\',\'' + product.id + '\',\'' + product.imageSrc + '\',' + discountedPrice + ')">Add to Cart</button>' +
            '</div>' +
            '</div>' +
            '</div>' +
            '</div>');

        // Append the card to the row
        $('#productRow').append(card);
    });
}


(function () {
    function search() {

        var searchTerm = document.getElementById('search-form').value.toLowerCase();
        // Get all products from JSON
        if (searchTerm == '') {
            location.reload();
        } else {
            document.getElementById("product-text").innerHTML = "Search Results From All Product Range";
            console.log(searchTerm);
            $.getJSON('../JSON/products.json', function (data) {
                var filteredProducts = [];

                // Iterate through all categories and products to find a match
                $.each(data, function (index, category) {
                    $.each(category, function (key, products) {
                        $.each(products, function (i, product) {
                            if (product.name.toLowerCase().includes(searchTerm)) {
                                filteredProducts.push(product);
                            }
                        });
                    });
                });
                console.log(filteredProducts);
                // Display filtered products

                $('#productRow').empty();
                displayProducts(filteredProducts);
            });
        }
    }

    var searchInput = document.getElementById('search-form');

    if (searchInput) {

        // input event for real-time search
        searchInput.addEventListener('input', search, true);

    }
    var searchBtn = document.getElementById('search-btn');

    if (searchBtn) {
        searchBtn.addEventListener('click', search, true);
    }
})();


function showCardDetails() {
    document.getElementById('cardDetails').style.display = 'block';
    document.getElementById('UpiDetails').style.display = 'none';
    document.getElementById('CODDetails').style.display = 'none';
}

function showUpiDetails() {
    document.getElementById('cardDetails').style.display = 'none';
    document.getElementById('UpiDetails').style.display = 'block';
    document.getElementById('CODDetails').style.display = 'none';
}

function showCOD() {
    document.getElementById('cardDetails').style.display = 'none';
    document.getElementById('UpiDetails').style.display = 'none';
    document.getElementById('CODDetails').style.display = 'block';
}



var rangeInput = document.getElementById('ratingRange');
var ratingValue = document.getElementById('ratingValue');


rangeInput.addEventListener('input', function () {

    ratingValue.textContent = rangeInput.value + " and above";
    console.log(rangeInput.value);
    filterAndDisplayProducts(rangeInput.value);
});

//  display products based on the rating range
function filterAndDisplayProducts(currentRating, data) {
    $.getJSON('../JSON/products.json', function (data) {
        var filteredProducts = [];

        if (currentPageCategory == "allProducts") {
            $.each(data, function (index, category) {
                // console.log(index);
                $.each(category, function (key, products) {
                    // console.log(category);
                    $.each(products, function (i, product) {
                        var productRating = parseInt(product.rating);
                        if (productRating >= currentRating) {
                            filteredProducts.push(product);
                        }
                    });
                });
            });
        }
        else {
            products = data[currentPageCategoryIndex][currentPageCategory];
            $.each(products, function (i, product) {
                var productRating = parseInt(product.rating);
                if (productRating >= currentRating) {
                    filteredProducts.push(product);
                }
            });
        }

        // Display filtered products
        $('#productRow').empty();
        displayProducts(filteredProducts);
    });

}
