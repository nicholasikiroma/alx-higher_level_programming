#!/usr/bin/node

function add (a, b) {
  if (arg1 && arg2) {
    console.log(arg1 + arg2);
  } else {
    console.log('NaN');
  }
}

const arg = process.argv;
const arg1 = parseInt(arg[2]);
const arg2 = parseInt(arg[3]);

add(arg1, arg2);
