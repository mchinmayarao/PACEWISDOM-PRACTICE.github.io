function login(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    console.log(username, password);

    $.getJSON('../JSON/users.json', function (data) {
        console.log(data);

        var hasMatch = false;

        for (var index = 0; index < data.length; ++index) {

            var user = data[index];
            if (user.username == username && user.password == password) {
                hasMatch = true;
                sessionStorage.setItem("currentUser", JSON.stringify(user));
                break;
            }
        }

        if (hasMatch) {
            alert("Valid Credentials");
            sessionStorage.setItem('isLoggedIn', 'true');
            window.location.href = '../html/allProducts.html';

        }
        else {

            alert("Invalid Credentials");
        }
    });
}

function accountButton() {
    var isLoggedIn = sessionStorage.getItem("isLoggedIn");
    if (isLoggedIn == 'true') {
        window.location.href = '../html/account.html';
    }
    else {
        alert("Login Required");
        window.location.href = '../html/login.html';
    }
}

var currentUser = JSON.parse(sessionStorage.getItem('currentUser'));
console.log(currentUser);


document.getElementById('firstName').value = currentUser.firstName;
document.getElementById('lastName').value = currentUser.lastName;
document.getElementById('email').value = currentUser.email;
document.getElementById('phoneNumber').value = currentUser.phone;
document.getElementById('address').value = currentUser.address;
document.getElementById('zip').value = currentUser.pinCode;

document.getElementById('user_username').innerHTML = currentUser.username;
document.getElementById('user_firstName').innerHTML = currentUser.firstName;
document.getElementById('user_lastName').innerHTML = currentUser.lastName;
document.getElementById('user_email').innerHTML = currentUser.email;
document.getElementById('user_phone').innerHTML = currentUser.phone;
document.getElementById('user_address').innerHTML = currentUser.address;
document.getElementById('user_pinCode').innerHTML = currentUser.pinCode;


function logOut() {
    alert("Logged Out");
    sessionStorage.setItem("isLoggedIn", 'false');
    sessionStorage.removeItem("currentUser");
    localStorage.removeItem("cartItems");
    localStorage.removeItem("finalPrice");
    window.location.href = '../html/index.html';
}

// const myModal = document.getElementById('myModal')
// const myInput = document.getElementById('myInput')

// myModal.addEventListener('shown.bs.modal', () => {
//     myInput.focus()
// })

function saveChanges(event) {
    event.preventDefault();

    currentUser.firstName = document.getElementById('firstName').value;
    currentUser.lastName = document.getElementById('lastName').value;
    currentUser.email = document.getElementById('email').value;
    currentUser.phone = document.getElementById('phoneNumber').value;
    currentUser.address = document.getElementById('address').value;
    currentUser.pinCode = document.getElementById('zip').value;

    sessionStorage.setItem('currentUser',JSON.stringify(currentUser));
    
    location.reload();
}