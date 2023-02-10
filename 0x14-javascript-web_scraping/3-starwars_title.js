#!/usr/bin/node
// Prints title of movie
const request = require('request');
const args = process.argv;

// Request URL

const url = 'https://swapi-api.alx-tools.com/api/films/' + `${args[2]}`;
request(url, (error, response, body) => {
  if (error) console.log(error);

  console.log(JSON.parse(body).title);
});
