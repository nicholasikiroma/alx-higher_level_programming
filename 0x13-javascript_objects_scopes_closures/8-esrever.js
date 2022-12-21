#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  let size = list.length;
  for (let start = 0; start < size; start += 1) {
    myList[start] = list[size - 1];
    size -= 1;
  }
  return myList;
};
