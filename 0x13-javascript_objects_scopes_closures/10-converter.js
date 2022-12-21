#!/usr/bin/node
exports.converter = function (base) {
  return function (val) {
    val.toString(base);
  };
};
