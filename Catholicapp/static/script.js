// script.js

function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username === "" || password === "") {
        alert("Please enter both username and password.");
        return false;
    }
    return true;
}

// Display registration message when form is successfully submitted
window.onload = function() {
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('registered') === 'true') {
        document.getElementById('registrationMessage').style.display = 'block';
    }
};
