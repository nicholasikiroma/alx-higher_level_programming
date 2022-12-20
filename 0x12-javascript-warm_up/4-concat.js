#!/usr/bin/node

const args = process.argv;

if (args[2]) {
  console.log(args[2] + ' is ' + args[3]);
} else {
  console.log('No argument');
}
