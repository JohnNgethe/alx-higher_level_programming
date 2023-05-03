const $ = window.$;

$(document).ready(function () {
  $.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', (data) => {
    $.each(data, (key, val) => {
      if (key === 'hello') {
        $('DIV#hello').text(val);
      }
    });
  });
});
