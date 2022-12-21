#!/usr/bin/node
/* A class Rectangle that defines a rectangle
 * If w or h is equal to 0 or not a positive integer, create an empty object
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
