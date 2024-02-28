var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

var tot_no_prd = Object.keys(cartItems).length;



console.log(tot_no_prd);

document.getElementById("tot_no_prd").innerHTML = tot_no_prd;

for(let i = 0; i<cartItems.length; i++){
    var cartItemElement = `<li class="list-group-item d-flex justify-content-between lh-sm">
    <div>
        <h6 class="my-0">${cartItems[i].productName}</h6>
        <small class="text-muted">${cartItems[i].quantity} x ₹ ${cartItems[i].productPrice}</small>
    </div>
    <span class="text-muted">₹ ${(cartItems[i].productPrice * cartItems[i].quantity)}</span>
</li>`;

$('#checkout_prd_list').append(cartItemElement);
}

var finalPrice = localStorage.getItem('finalPrice');
console.log('Final Price from localStorage:', finalPrice);
document.getElementById("FinalPrice").innerHTML = "₹ " + finalPrice;