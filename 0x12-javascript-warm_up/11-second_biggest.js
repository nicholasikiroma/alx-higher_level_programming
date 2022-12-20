#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  const arr = args.slice(2).map(Number);
  const num = arr.sort(function (a, b) { return b - a; })[1];
  console.log(num);
}
