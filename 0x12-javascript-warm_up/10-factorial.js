#!/usr/bin/node

function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const args = process.argv;
const arg = parseInt(args[2]);
console.log(factorial(arg));
