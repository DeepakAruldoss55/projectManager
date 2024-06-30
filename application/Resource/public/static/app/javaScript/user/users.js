// JavaScript (users.js)

let currentPage = 1;
let rowsPerPage = 10;
let totalPages;
const pageNumbers = document.getElementById("pageNumbers");

function paginateTable() {
    let table = document.getElementById("userTable");
    let rows = Array.from(table.rows).slice(1);
    totalPages = Math.ceil(rows.length / rowsPerPage);

    rows.forEach(row => row.style.display = "none");

    let start = (currentPage - 1) * rowsPerPage;
    let end = start + rowsPerPage;
    rows.slice(start, end).forEach(row => row.style.display = "");
    pageNumbers.innerHTML = "";
    createPageLink("<<", 1);
    createPageLink("<", currentPage - 1);

    let startPageNumber = currentPage < 5 ? 1 : (currentPage > totalPages - 2 ? totalPages - 4 : currentPage - 2);
    let endPageNumber = totalPages < 5 ? totalPages : (currentPage <= totalPages - 2 ? startPageNumber + 4 : totalPages);
    for (let i = startPageNumber; i <= endPageNumber; i++) {
        createPageLink(i, i);
    }
    createPageLink(">", currentPage + 1);
    createPageLink(">>", totalPages);

    setActivePageNumber();
    from.innerHTML = (currentPage - 1) * rowsPerPage + 1;
    to.innerHTML = currentPage === totalPages ? rows.length : (currentPage) * rowsPerPage;
    totalTableEntries.innerHTML = rows.length;
}

paginateTable();

function changePage(e, pageNumber) {
    if ((pageNumber == 0) || (pageNumber == totalPages + 1)) return;
    e.preventDefault();
    currentPage = pageNumber;
    pageNumberInput.value = "";
    paginateTable();
}

function setActivePageNumber() {
    document.querySelectorAll("#pageNumbers a").forEach(a => {
        if (a.innerText == currentPage) {
            a.classList.add("active");
        } else {
            a.classList.remove("active");
        }
    });
}

function createPageLink(linkText, pageNumber) {
    let pageLink = document.createElement("a");
    pageLink.href = "#";
    pageLink.innerHTML = linkText;
    pageLink.addEventListener("click", function(e) {
        changePage(e, pageNumber);
    });
    pageNumbers.appendChild(pageLink);
}

goToPageButton.addEventListener("click", (e) => {
    changePage(e, pageNumberInput.value);
});

pageNumberInput.addEventListener("keypress", function(e) {
    if (e.which === 13) {
        changePage(e, pageNumberInput.value);
    }
});

// Add this JavaScript to handle dropdown functionality
function toggleDropdown(button) {
    var dropdownContent = button.nextElementSibling;
    dropdownContent.classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.closest('.dropbtn')) {
        closeAllDropdowns();
    }

    // Close delete modal if clicked outside
    if (event.target === deleteModal) {
        deleteModal.style.display = "none";
    }
}

// Function to close all dropdowns
function closeAllDropdowns() {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
    }
}

function viewItem(id) {
    window.location.href = '/viewProfile/' + id;
}

function editItem(id) {
    window.location.href = '/updateUser/' + id;
}

// Handle delete modal
var deleteModal = document.getElementById("deleteModal");
var span = deleteModal.querySelector(".close");
var confirmDeleteButton = document.getElementById("confirmDeleteButton");
var deleteItemId;

function deleteItem(id) {
    closeAllDropdowns();
    deleteItemId = id;
    deleteModal.style.display = "block";
}

span.onclick = function() {
    deleteModal.style.display = "none";
}

document.getElementById("cancelDeleteButton").onclick = function() {
    deleteModal.style.display = "none";
}

// Confirm delete and close modal
confirmDeleteButton.onclick = function() {
    deleteModal.style.display = "none";
    sendDeleteRequest(deleteItemId);
}

// Function to send delete request through AJAX
function sendDeleteRequest(id) {
    fetch(`/deleteUser/${id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        location.reload();
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}

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
