#!/usr/bin/node
/* A class Rectangle that defines a rectangle
 * If w or h is equal to 0 or not a positive integer, create an empty object
 */
const SquareV2 = require('./5-square');

class Square extends SquareV2 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i += 1) {
      let char = '';
      for (let k = 0; k < this.width; k += 1) {
        char += c;
      }
      console.log(char);
    }
  }
}
module.exports = Square;
