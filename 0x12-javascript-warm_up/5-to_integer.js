#!/usr/bin/node

const args = process.argv;

const parsed = parseInt(args[2]);

if (parsed) {
  console.log('My number: %i', parsed);
} else {
  console.log('Not a number');
}
