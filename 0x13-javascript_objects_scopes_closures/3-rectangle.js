#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
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
module.exports = Rectangle;
