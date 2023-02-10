#!/usr/bin/node
const request = require('request');
const args = process.argv;

// Request URL
const url = `${args[2]}`;

request(url, (error, response, body) => {
  if (error) console.log(error);

  console.log('Code:', response.statusCode);
});
