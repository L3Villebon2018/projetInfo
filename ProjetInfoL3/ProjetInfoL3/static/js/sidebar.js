$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('.content').toggleClass('active');
        $('#sidebar').toggleClass('active');

    });

});