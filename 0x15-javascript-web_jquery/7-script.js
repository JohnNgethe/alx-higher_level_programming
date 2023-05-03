const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.getJSON(url, (data) => {
  $.each(data, (key, val) => {
    if (key === 'name') {
      $('DIV#character').text(val);
    }
  });
});
