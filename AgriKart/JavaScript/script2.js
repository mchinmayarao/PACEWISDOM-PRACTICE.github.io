
function addToCart(productName, productId, productImageSrc, productPrice) {


    var isLoggedIn = sessionStorage.getItem("isLoggedIn");

    if(isLoggedIn == "true"){
        var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

        // Check if the product is already in the cart
        var existingItem = cartItems.find(item => item.productId === productId);
    
        if (existingItem) {
            alert('Item ' + productName + ' is already in the cart!');
        } else {
            var cartItem = {
                productName: productName,
                productId: productId,
                productImageSrc: productImageSrc,
                productPrice: productPrice,
                quantity: 1
            };
    
            cartItems.push(cartItem);
            localStorage.setItem('cartItems', JSON.stringify(cartItems));
            alert('Added ' + productName + ' to the cart!');
            location.reload();
        }
    }

    else{
        alert("Login Required !");
        window.location.href = '../html/login.html';
    }
   
}




var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
var cartItemCount = cartItems.length;
// Update the cart badge content
$('#cartItemCount').text(cartItemCount);


function priceUpdate(index) {
    let quantity = document.querySelector('.form-select[data-index="' + index + '"]').value;
    cartItems[index].quantity = quantity;
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    location.reload();

}

function renderCartItems(cartItem, i) {
    var cartItemElement = $('<div class="row gy-3 mb-4">' +
        '<div class="col-lg-5">' +
        '<div class="me-lg-5">' +
        '<div class="d-flex">' +
        '<img src=../' + cartItem.productImageSrc + ' class="border rounded me-3" style="width: 96px; height: 96px;" />' +
        '<div class="">' +
        '<a href="#" class="nav-link">' + cartItem.productName + '</a>' +
        '<p class="text-muted">' + 'Product ID: ' + cartItem.productId + '</p>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '<div class="col-lg-2 col-sm-6 col-6 d-flex flex-row flex-lg-column flex-xl-row text-nowrap">' +
        '<div class="">' +
        '<select style="width: 100px;" class="form-select me-4" data-index="' + i + '" onchange="priceUpdate(' + i +')">' +
        '<option value="1" ' + (cartItem.quantity == 1 ? 'selected' : '') + '>1</option>' +
        '<option value="2" ' + (cartItem.quantity == 2 ? 'selected' : '') + '>2</option>' +
        '<option value="3" ' + (cartItem.quantity == 3 ? 'selected' : '') + '>3</option>' +
        '<option value="4" ' + (cartItem.quantity == 4 ? 'selected' : '') + '>4</option>' +
        '<option value="5" ' + (cartItem.quantity == 5 ? 'selected' : '') + '>5</option>' +
        '<option value="6" ' + (cartItem.quantity == 6 ? 'selected' : '') + '>6</option>' +
        '<option value="7" ' + (cartItem.quantity == 7 ? 'selected' : '') + '>7</option>' +
        '<option value="8" ' + (cartItem.quantity == 8 ? 'selected' : '') + '>8</option>' +
        '<option value="9" ' + (cartItem.quantity == 9 ? 'selected' : '') + '>9</option>' +
        '<option value="10" ' + (cartItem.quantity == 10 ? 'selected' : '') + '>10</option>' +
        '</select>' +
        '</div>' +
        '<div class="">' +
        '<text class="h6" id = "totPrice_' + i + '"> ₹ ' + (cartItem.productPrice * cartItem.quantity) + '</text> <br />' +
        '<small class="text-muted text-nowrap">₹ ' + cartItem.productPrice + ' / per item </small>' +
        '</div>' +
        '</div>' +
        '<div class="col-lg col-sm-6 d-flex justify-content-sm-center justify-content-md-start justify-content-lg-center justify-content-xl-end mb-2">' +
        '<div class="float-md-end">' +
        '<a href="#" class="btn btn-light border text-danger icon-hover-danger" onclick="removeFromCart(' + i + ')"> Remove</a>' +
        '</div>' +
        '</div>' +
        '</div>');

    return cartItemElement;

}

// display cart items
for (let i = 0; i < cartItems.length; i++) {

    cartItemElement = renderCartItems(cartItems[i], i);

    $('#cartItems').append(cartItemElement);


}

// total price calculation
function totPrice_cal(){
    var totPrice = 0;
    for (let i = 0; i < cartItems.length; i++) {
        totPrice += (cartItems[i].productPrice * cartItems[i].quantity);
    }

    return totPrice;
}

// remove item from the cart 
function removeFromCart(index) {
    cartItems.splice(index, 1);
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    location.reload();
}

var totPrice = totPrice_cal();

// Calculate discount, tax, and finalPrice
var discount = parseFloat((0.05 * totPrice).toFixed(2));
var tax = parseFloat((0.18 * totPrice).toFixed(2));
var finalPrice = parseFloat((totPrice - discount + tax).toFixed(2));

// Set values only if corresponding elements exist
var totPriceElement = document.getElementById('totPrice');
var discountElement = document.getElementById('Discount');
var taxElement = document.getElementById('tax');
var finalPriceElement = document.getElementById('finalPrice');

if (totPriceElement) {
    totPriceElement.innerHTML = "₹ " + totPrice;
}

if (discountElement) {
    discountElement.innerHTML = "₹ - " + discount;
}

if (taxElement) {
    taxElement.innerHTML = "₹ + " + tax;
}

if (finalPriceElement) {
    finalPriceElement.innerHTML = "₹ " + finalPrice;
}


function makePurchase(){
    if(finalPrice == 0){
        alert("Cart Is Empty. Add some item to cart first!");
        window.location.href = '../html/allProducts.html';

    }
    else{
        window.location.href = '../html/checkout.html';
    }
}

// Store finalPrice in localStorage
localStorage.setItem('finalPrice', finalPrice);


