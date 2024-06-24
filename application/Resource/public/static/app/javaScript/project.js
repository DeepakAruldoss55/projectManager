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
