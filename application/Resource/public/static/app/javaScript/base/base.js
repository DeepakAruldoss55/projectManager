document.addEventListener('DOMContentLoaded', function() {
    // Function to apply the collapsed state
    function applyCollapsedState() {
        const sidebarContainer = document.getElementById('sidebar-container');
        const mainContent = document.querySelector('.main-content');

        sidebarContainer.classList.add('sidebar-collapsed');
        sidebarContainer.classList.remove('sidebar-expanded');
        mainContent.classList.add('collapsed');

        document.querySelectorAll('.menu-collapsed').forEach(function(element) {
            element.classList.add('d-none');
        });

        document.querySelectorAll('.sidebar-submenu').forEach(function(element) {
            element.classList.add('d-none');
        });

        document.querySelectorAll('.submenu-icon').forEach(function(element) {
            element.classList.add('d-none');
        });

        const separatorTitles = document.querySelectorAll('.sidebar-separator-title');
        separatorTitles.forEach(function(element) {
            element.classList.remove('d-flex');
        });

        const collapseIcon = document.getElementById('collapse-icon');
        collapseIcon.classList.remove('fa-angle-double-left');
        collapseIcon.classList.add('fa-angle-double-right');
    }

    // Check the initial state from localStorage and apply it
    const isSidebarCollapsed = localStorage.getItem('sidebar-collapsed') === 'true';
    if (isSidebarCollapsed) {
        applyCollapsedState();
    }

    // Remove no-transition class after initial state is set
    setTimeout(() => {
        document.getElementById('sidebar-container').classList.remove('no-transition');
        document.querySelector('.main-content').classList.remove('no-transition');
    }, 10);

    // Toggle sidebar collapse
    document.querySelectorAll('[data-toggle=sidebar-colapse]').forEach(function(element) {
        element.addEventListener('click', function() {
            toggleSidebar();
        });
    });

    function toggleSidebar() {
        const sidebarContainer = document.getElementById('sidebar-container');
        const mainContent = document.querySelector('.main-content');
        const isCollapsed = sidebarContainer.classList.contains('sidebar-collapsed');

        sidebarContainer.classList.toggle('sidebar-expanded');
        sidebarContainer.classList.toggle('sidebar-collapsed');
        mainContent.classList.toggle('collapsed');

        document.querySelectorAll('.menu-collapsed').forEach(function(element) {
            element.classList.toggle('d-none');
        });

        document.querySelectorAll('.sidebar-submenu').forEach(function(element) {
            element.classList.toggle('d-none');
        });

        document.querySelectorAll('.submenu-icon').forEach(function(element) {
            element.classList.toggle('d-none');
        });

        const separatorTitles = document.querySelectorAll('.sidebar-separator-title');
        separatorTitles.forEach(function(element) {
            element.classList.toggle('d-flex');
        });

        const collapseIcon = document.getElementById('collapse-icon');
        collapseIcon.classList.toggle('fa-angle-double-left');
        collapseIcon.classList.toggle('fa-angle-double-right');

        // Save the collapse state in localStorage
        localStorage.setItem('sidebar-collapsed', !isCollapsed);
    }

    // Highlight active menu item based on current URL
    var path = window.location.pathname;
    var userPaths = ['/users/', '/adduser/', /^\/viewProfile\/\d+$/];
    var clientPaths = ['/clientsList/', '/addclient/'];

    document.querySelectorAll('a[href="' + path + '"]').forEach(function(element) {
        element.classList.add('active');
    });

    if (userPaths.some(function(p) { return p instanceof RegExp ? p.test(path) : p === path; })) {
        document.querySelectorAll('a[href="/users/"]').forEach(function(element) {
            element.classList.add('active');
        });
    }

    if (clientPaths.some(function(p) { return p instanceof RegExp ? p.test(path) : p === path; })) {
        document.querySelectorAll('a[href="/clientsList/"]').forEach(function(element) {
            element.classList.add('active');
        });
    }
});
