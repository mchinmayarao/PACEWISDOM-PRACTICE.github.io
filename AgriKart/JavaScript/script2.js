
function addToCart(productName, productId, productImageSrc, productPrice) {
    var cartItem = {
        productName: productName,
        productId: productId,
        productImageSrc: productImageSrc,
        productPrice: productPrice
    };

    var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    cartItems.push(cartItem);
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    alert('Added ' + productName + ' to the cart!');
}

var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];


for(let i = 0; i<cartItems.length;i++) {
    var cartItem = cartItems[i];
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
        '<select style="width: 100px;" class="form-select me-4">' +
        '<option>1</option>' +
        '<option>2</option>' +
        '<option>3</option>' +
        '<option>4</option>' +
        '</select>' +
        '</div>' +
        '<div class="">' +
        '<text class="h6"> ₹ ' + cartItem.productPrice + '</text> <br />' +
        '<small class="text-muted text-nowrap">₹ ' + cartItem.productPrice + ' / per item </small>' +
        '</div>' +
        '</div>' +
        '<div class="col-lg col-sm-6 d-flex justify-content-sm-center justify-content-md-start justify-content-lg-center justify-content-xl-end mb-2">' +
        '<div class="float-md-end">' +
        '<a href="#" class="btn btn-light border text-danger icon-hover-danger" onclick="removeFromCart(' + i + ')"> Remove</a>' +
        '</div>' +
        '</div>' +
        '</div>');

    $('#cartItems').append(cartItemElement);
}

function removeFromCart(index) {
    cartItems.splice(index, 1);
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    location.reload(); // Refresh the page to reflect the updated cart
}