
$(document).ready(function () {
    //  see http://momentjs.com/ for format details
    var html = $('html');
    var lang = html.attr('lang');
    var date_format = html.attr('data-date-format');
    console.log(date_format);

    $('.date_picker').datetimepicker({
        allowInputToggle: true,
        format: date_format,
        locale: lang

    });

});
