#!/usr/bin/node
const SquareA = require('./5-square.js');
module.exports = class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let space = '';
      for (let i = 0; i < this.width; i++) {
        space += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(space);
      }
    }
  }
};
