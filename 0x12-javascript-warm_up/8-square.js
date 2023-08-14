#!/usr/bin/node
let i = 0;
let n = 0;
let t = '';
const a = parseInt(process.argv[2]);
if (a) {
  if (a > 0) {
    while (n < a) {
      while (i < a) {
        t = t.concat('X');
        i++;
      }
      console.log(t);
      n++;
    }
  }
} else if (a !== 0) { console.log('Missing size'); }
