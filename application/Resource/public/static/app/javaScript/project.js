let currentPage = 1;
let rowsPerPage = 10;
let totalPages;
const pageNumbers = document.getElementById("pageNumbers");

function paginateTable() {
    let table = document.getElementById("projectTable");
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

document.addEventListener('DOMContentLoaded', function() {
    var offcanvasAddProject = document.getElementById('offcanvasAddProject');
    var pageOverlay = document.getElementById('pageOverlay');
    
    document.getElementById('addProjectButton').addEventListener('click', function() {
        offcanvasAddProject.classList.add('show');
        pageOverlay.classList.add('show');
    });

    document.querySelector('.offcanvas .close').addEventListener('click', function() {
        offcanvasAddProject.classList.remove('show');
        pageOverlay.classList.remove('show');
    });

    // Add an event listener to the Cancel button
    document.getElementById('addProjectCancelButton').addEventListener('click', function() {
        offcanvasAddProject.classList.remove('show');
        pageOverlay.classList.remove('show');
    });

    // Hide the offcanvas and overlay when clicking on the overlay
    pageOverlay.addEventListener('click', function() {
        offcanvasAddProject.classList.remove('show');
        pageOverlay.classList.remove('show');
    });
});
