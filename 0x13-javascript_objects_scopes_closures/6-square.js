#!/usr/bin/node
// class Square that defines square
const mySquare = require('./5-square');

class Square extends mySquare {
  charPrint (c) {
    if (c == undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
