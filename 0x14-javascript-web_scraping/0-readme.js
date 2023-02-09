#!/usr/bin/node
// Reads a file
const fs = require('fs');
const args = process.argv;

fs.readFile(`${args[2]}`, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
