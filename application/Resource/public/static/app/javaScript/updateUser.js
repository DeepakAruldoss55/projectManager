document.addEventListener('DOMContentLoaded', function() {
    const updateUserForm = document.getElementById('updateUserForm');
    const userId = document.getElementById('userId').value;  // Get userId from hidden input field
    updateUserForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(updateUserForm);
        fetch(`/updateUser/${userId}`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.text().then(text => { throw new Error(text) })
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                // alert('User updated successfully');
                // window.location.href = '/users';
            } else {
                console.error('Update failed:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));
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
