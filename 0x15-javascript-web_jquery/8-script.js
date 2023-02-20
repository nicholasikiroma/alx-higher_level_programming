const titleTag = $('UL#list_movies');
const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(URL, function (data) {
    data.results.forEach(function (movie) {
        const title = movie.title;
        titleTag.append('<li>' + title + '</li>');
    });
});
