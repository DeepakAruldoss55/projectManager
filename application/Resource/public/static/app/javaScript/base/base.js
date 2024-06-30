document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar collapse
    document.querySelectorAll('[data-toggle=sidebar-colapse]').forEach(function(element) {
        element.addEventListener('click', function() {
            SidebarCollapse();
        });
    });

    function SidebarCollapse() {
        document.querySelectorAll('.menu-collapsed').forEach(function(element) {
            element.classList.toggle('d-none');
        });
        document.querySelectorAll('.sidebar-submenu').forEach(function(element) {
            element.classList.toggle('d-none');
        });
        document.querySelectorAll('.submenu-icon').forEach(function(element) {
            element.classList.toggle('d-none');
        });
        var sidebarContainer = document.getElementById('sidebar-container');
        sidebarContainer.classList.toggle('sidebar-expanded');
        sidebarContainer.classList.toggle('sidebar-collapsed');

        var separatorTitles = document.querySelectorAll('.sidebar-separator-title');
        separatorTitles.forEach(function(element) {
            element.classList.toggle('d-flex');
        });

        var collapseIcon = document.getElementById('collapse-icon');
        collapseIcon.classList.toggle('fa-angle-double-left');
        collapseIcon.classList.toggle('fa-angle-double-right');
    }

    // Highlight active menu item based on current URL
    var path = window.location.pathname;
    var userPaths = ['/users/', '/adduser/', /^\/viewProfile\/\d+$/];

    document.querySelectorAll('a[href="' + path + '"]').forEach(function(element) {
        element.classList.add('active');
    });

    if (userPaths.some(function(p) { return p instanceof RegExp ? p.test(path) : p === path; })) {
        document.querySelectorAll('a[href="/users/"]').forEach(function(element) {
            element.classList.add('active');
        });
    }

    
});
