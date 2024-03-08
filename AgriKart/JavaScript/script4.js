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
