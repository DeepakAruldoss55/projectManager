document.addEventListener('DOMContentLoaded', function() {
    const updateUserForm = document.getElementById('updateUserForm');
    const userId = document.getElementById('userId').value;
    const loadingScreen = document.getElementById('loadingScreen');
    function showSuccess(message) {
        var successMessage = document.getElementById('successMessage');
        successMessage.textContent = message;
        successMessage.classList.remove('hide');
        successMessage.classList.add('show');
        setTimeout(function() {
            successMessage.classList.remove('show');
            successMessage.classList.add('hide');
        }, 2000);
    }

    updateUserForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(updateUserForm);
        loadingScreen.style.display = 'flex';
        fetch(`/updateUser/${userId}`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: formData
        })
        .then(response => {
            loadingScreen.style.display = 'none';
            if (!response.ok) {
                return response.text().then(text => { throw new Error(text) });
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                showSuccess('Update');
            } else {
                showSuccess('Update failed:', data.error);
            }
        })
        .catch(error => {
            loadingScreen.style.display = 'none';
            showSuccess('Error:', error);
        });
    });
});

// Utility function to get the CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
