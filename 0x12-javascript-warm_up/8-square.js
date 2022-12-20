#!/usr/bin/node

const arg = process.argv;
let i = 0;

const parsed = parseInt(arg[2]);

if (isNaN(parsed)) {
  console.log('Missing size');
}
while (i < parsed) {
  console.log('X'.repeat(parsed));
  i += 1;
}
