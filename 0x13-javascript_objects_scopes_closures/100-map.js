#!/usr/bin/node
const list = require('./100-data').list;
const myList = list.map(function (num, index) {
  return num * index;
});

console.log(list);
console.log(myList);
