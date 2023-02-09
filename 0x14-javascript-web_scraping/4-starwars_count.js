#!/usr/bin/node
// counts occurrence of "Wedge Antilles"

const request = require('request');
// Request URL

const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) console.log(error);
  const content = JSON.parse(body);
  let movies = content.results;
  movies = movies.filter(
    film => film.characters.find(
      character => character.match(/18/)
    )
  );
  console.log(movies.length);
});
