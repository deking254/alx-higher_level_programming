#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let i = 0;
      let n = 0;
      let st = '';
      const a = this.width;
      const b = this.height;
      while (i < b) {
        while (n < a) {
          st = st + c;
          n++;
        }
        console.log(st);
        i++;
      }
    } else {
      let i = 0;
      let n = 0;
      let st = '';
      const a = this.width;
      const b = this.height;
      while (i < b) {
        while (n < a) {
          st = st + 'X';
          n++;
        }
        console.log(st);
        i++;
      }
    }
  }
}
module.exports = Square;
