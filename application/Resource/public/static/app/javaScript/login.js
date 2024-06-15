document.addEventListener('DOMContentLoaded', function() {
    function showError(message) {
        var errorMessage = document.getElementById('errorMessage');
        errorMessage.textContent = message;
        errorMessage.classList.remove('hide');
        errorMessage.classList.add('show');
        setTimeout(function() {
            errorMessage.classList.remove('show');
            errorMessage.classList.add('hide');
        }, 2000);
    }

    function login() {
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;
        var loadingScreen = document.getElementById('loadingScreen');

        loadingScreen.style.display = 'flex';

        var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/login/', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 400) {
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    window.location.href = '/dashboard/';
                } else {
                    loadingScreen.style.display = 'none';
                    showError('Invalid username or password');
                }
            } else {
                loadingScreen.style.display = 'none';
                showError('An error occurred. Please try again');
            }
        };

        xhr.onerror = function() {
            loadingScreen.style.display = 'none';
            showError('An error occurred. Please try again');
        };

        xhr.send('username=' + encodeURIComponent(username) + 
                 '&password=' + encodeURIComponent(password) + 
                 '&csrfmiddlewaretoken=' + encodeURIComponent(csrfToken));
    }

    var loginButton = document.getElementById('loginButton');
    loginButton.addEventListener('click', function() {
        login();
    });

    document.addEventListener('keypress', function(e) {
        if (e.which === 13) {
            login();
        }
    });
});
