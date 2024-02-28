
function addToCart(productName, productId, productImageSrc, productPrice) {
    var cartItem = {
        productName: productName,
        productId: productId,
        productImageSrc: productImageSrc,
        productPrice: productPrice,
        quantity:1
    };

    var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    cartItems.push(cartItem);
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    alert('Added ' + productName + ' to the cart!');
}

var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

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

for (let i = 0; i < cartItems.length; i++) {

    cartItemElement = renderCartItems(cartItems[i], i);

    $('#cartItems').append(cartItemElement);


}


function totPrice_cal(){
    var totPrice = 0;
    for (let i = 0; i < cartItems.length; i++) {
        totPrice += (cartItems[i].productPrice * cartItems[i].quantity);
    }

    return totPrice;
}
function removeFromCart(index) {
    cartItems.splice(index, 1);
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    location.reload();
}

var totPrice = totPrice_cal();
var discount = parseFloat((0.05 * totPrice).toFixed(2));
var tax = parseFloat((0.18 * totPrice).toFixed(2));
var finalPrice = totPrice - discount + tax;
document.getElementById("totPrice").innerHTML = "₹ " + totPrice;
document.getElementById("Discount").innerHTML = "₹ - " + discount;
document.getElementById("tax").innerHTML = "₹ + " + tax;
document.getElementById("finalPrice").innerHTML = "₹ + " + finalPrice;

