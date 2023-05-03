const $ = window.$;

$('DIV#toggle_header').on('click', function toggleClass () {
  if ($(this).hasClass('red') && !$(this).hasClass('green')) {
    $(this).removeClass('red');
    $(this).addClass('green');
  } else {
    $(this).removeClass('green');
    $(this).addClass('red');
  }
});
