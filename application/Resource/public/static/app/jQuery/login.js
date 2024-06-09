$(document).ready(function() {
    $('#loginButton').on('click', function() {
        const username = $('#username').val();
        const password = $('#password').val();

        $.ajax({
            type: 'POST',
            url: '/login/',
            data: {
                'username': username,
                'password': password,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.success) {
                    console.log('logged in');
                    window.location.href = '/dashboard/';
                } else {
                    console.log('login failed: ' + response.error);
                }
            },
            error: function(error) {
                console.log('error', error);
            }
        });
    });
});
