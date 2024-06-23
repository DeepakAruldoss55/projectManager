document.addEventListener('DOMContentLoaded', function() {
    var offcanvasRight = document.getElementById('offcanvasRight');
    var pageOverlay = document.getElementById('pageOverlay');
    
    document.getElementById('addProjectButton').addEventListener('click', function() {
        offcanvasRight.classList.add('show');
        pageOverlay.classList.add('show');
    });

    document.querySelector('.offcanvas .close').addEventListener('click', function() {
        offcanvasRight.classList.remove('show');
        pageOverlay.classList.remove('show');
    });

    // Add an event listener to the Cancel button
    document.getElementById('addProjectCancelButton').addEventListener('click', function() {
        offcanvasRight.classList.remove('show');
        pageOverlay.classList.remove('show');
    });

    // Hide the offcanvas and overlay when clicking on the overlay
    pageOverlay.addEventListener('click', function() {
        offcanvasRight.classList.remove('show');
        pageOverlay.classList.remove('show');
    });
});
