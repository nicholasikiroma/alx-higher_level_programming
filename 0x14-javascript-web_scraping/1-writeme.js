#!/usr/bin/node
// Writes text to a file

const fs = require('fs');
const args = process.argv;

const content = `${args[3]}`;

fs.writeFile(`${args[2]}`, content, err => {
  if (err) {
    console.error(err);
  }
});
