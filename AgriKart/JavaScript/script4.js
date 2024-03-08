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
            if(user.username == username && user.password == password){
                hasMatch = true;
                sessionStorage.setItem("currentUser",JSON.stringify(user));
                break;
            }
        }

        if(hasMatch){
            alert("Valid Credentials");
            sessionStorage.setItem('isLoggedIn','true');
            window.location.href = '../html/allProducts.html';
            
        }
        else{
            
            alert("Invalid Credentials");
        }
    });
}

function accountButton(){
    var isLoggedIn = sessionStorage.getItem("isLoggedIn");
    if(isLoggedIn == 'true'){
        window.location.href = '../html/account.html';
    }
    else{
        alert("Login Required");
        window.location.href = '../html/login.html';
    }
}

var currentUser = JSON.parse(sessionStorage.getItem('currentUser'));
console.log(currentUser);


document.getElementById('user_username').innerHTML = currentUser.username;
document.getElementById('user_firstName').innerHTML = currentUser.firstName;
document.getElementById('user_lastName').innerHTML = currentUser.lastName;
document.getElementById('user_email').innerHTML = currentUser.email;
document.getElementById('user_phone').innerHTML = currentUser.phone;
document.getElementById('user_address').innerHTML = currentUser.address;
document.getElementById('user_pinCode').innerHTML = currentUser.pinCode;

function logOut(){
    alert("Logged Out");
    sessionStorage.setItem("isLoggedIn",'false');
    sessionStorage.removeItem("currentUser");
    window.location.href = '../html/index.html';
}