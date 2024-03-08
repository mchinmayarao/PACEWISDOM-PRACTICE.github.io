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

//console.log(currentUser);



function validateForm() {
    // Get all the required input elements
    const firstName = document.getElementById('firstName');
    const lastName = document.getElementById('lastName');
    const phoneNumber = document.getElementById('phoneNumber');
    const address = document.getElementById('address');
    const zip = document.getElementById('zip');

    const ccName = document.getElementById('cc-name');
    const ccNumber = document.getElementById('cc-number');
    const ccExpiration = document.getElementById('cc-expiration');
    const ccCvv = document.getElementById('cc-cvv');

    const upiId = document.getElementById('upi-id');

    // Check if all required fields are filled
    if (
        validateInput(firstName) &&
        validateInput(lastName) &&
        validateInput(phoneNumber) &&
        validateInput(address) &&
        validateInput(zip) &&
        (document.getElementById('credit').checked ? validateInput(ccName) && validateInput(ccNumber) && validateInput(ccExpiration) && validateInput(ccCvv) : true) &&
        (document.getElementById('debit').checked ? validateInput(upiId) : true)
    ) {
        // If all validations pass, redirect to successPage.html
        window.location.href = './html/successPage.html';
    }
}




function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    // Get all form elements
    const form = document.querySelector('.needs-validation');
    const firstName = document.getElementById('firstName');
    const lastName = document.getElementById('lastName');
    const email = document.getElementById('email');
    const phoneNumber = document.getElementById('phoneNumber');
    const address = document.getElementById('address');
    const zip = document.getElementById('zip');
    const ccName = document.getElementById('cc-name');
    const ccNumber = document.getElementById('cc-number');
    const ccExpiration = document.getElementById('cc-expiration');
    const ccCvv = document.getElementById('cc-cvv');
    const upiId = document.getElementById('upi-id');

    // Reset all validation messages
    resetValidationMessages(form);

    // Validate fields and display error messages if any
    let isValid = true;

    if (firstName.value === "") {
        firstName.classList.add('is-invalid');
        isValid = false;
    }

    if (lastName.value === "") {
        lastName.classList.add('is-invalid');
        isValid = false;
    }

    if (email.value == "" && !validateEmail(email.value)) {
        email.classList.add('is-invalid');
        isValid = false;
    }

    if (phoneNumber.value === "" || !/^[0-9]{10}$/.test(phoneNumber.value)) {
        phoneNumber.classList.add('is-invalid');
        isValid = false;
    }

    if (address.value === "") {
        address.classList.add('is-invalid');
        isValid = false;
    }

    if (zip.value === "" || !/^[0-9]{6}$/.test(zip.value)) {
        zip.classList.add('is-invalid');
        isValid = false;
    }

    const selectedPayment = document.querySelector('input[name="paymentMethod"]:checked');

    if (selectedPayment.id === "credit") {
        if (ccName.value === "") {
            ccName.classList.add('is-invalid');
            isValid = false;
        }

        if (ccNumber.value === "" || !/^[0-9]{16}$/.test(ccNumber.value)) {
            ccNumber.classList.add('is-invalid');
            isValid = false;
        }

        if (ccExpiration.value === "" || !/^[0-9]{4}$/.test(ccExpiration.value) || parseInt(ccExpiration.value) < new Date().getFullYear()) {
            ccExpiration.classList.add('is-invalid');
            isValid = false;
        }

        if (ccCvv.value === "" || !/^[0-9]{3}$/.test(ccCvv.value)) {
            ccCvv.classList.add('is-invalid');
            isValid = false;
        }
    } else if (selectedPayment.id === "debit") {
        if (upiId.value === "" || !/^[\w.-]+@[\w.-]+$/.test(upiId.value)) {
            upiId.classList.add('is-invalid');
            isValid = false;
        }
    }

    // If all fields are valid, submit the form and redirect
    if (isValid) {
        form.submit(); // Removed event.preventDefault() as the form is valid
        window.location.href = "successPage.html"; // Redirect to success page
    }
}

function resetValidationMessages(form) {
    const invalidFields = form.querySelectorAll('.is-invalid');
    for (const field of invalidFields) {
        field.classList.remove('is-invalid');
    }
}

function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}
