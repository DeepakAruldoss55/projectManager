$(document).ready(function() {
    $('[data-toggle=sidebar-colapse]').click(function() {
        SidebarCollapse();
    });

    function SidebarCollapse() {
        $('.menu-collapsed').toggleClass('d-none');
        $('.sidebar-submenu').toggleClass('d-none');
        $('.submenu-icon').toggleClass('d-none');
        $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');

        var SeparatorTitle = $('.sidebar-separator-title');
        if (SeparatorTitle.hasClass('d-flex')) {
            SeparatorTitle.removeClass('d-flex');
        } else {
            SeparatorTitle.addClass('d-flex');
        }
        $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
    }

    // Highlight active menu item based on current URL
    var path = window.location.pathname;
    var userPaths = ['/users/', '/adduser/', /^\/viewProfile\/\d+$/];

    $('a[href="' + path + '"]').addClass('active');

    if (userPaths.some(function(p) { return p instanceof RegExp ? p.test(path) : p === path; })) {
        $('a[href="/users/"]').addClass('active');
    }
});