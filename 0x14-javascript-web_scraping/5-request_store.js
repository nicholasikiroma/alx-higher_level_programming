#!/usr/bin/node
// Stores content of web page in a file
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const file = args[3];

request(url, (error, response, body) => {
  if (error) console.log(error);

  fs.writeFile(file, body, 'utf-8', err => {
    if (err) console.error(err);
  });
});
