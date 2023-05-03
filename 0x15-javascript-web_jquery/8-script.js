const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.getJSON(url, (data) => {
  data.results.forEach(items => {
    $('UL#list_movies').append(`<li>${items.title}</li>`);
  });
});
