#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let item = 0; item < list.length; item += 1) {
    if (list[item] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
