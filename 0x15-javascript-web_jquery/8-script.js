/*
   fetches and lists the title for all movies by using URL
*/
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data, textStatus) {
  data.results.map((movie) => $('UL#list_movies').append('<li>' + movie.title + '</li>'));
});