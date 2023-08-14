#!/usr/bin/node
let a = 1;
let c = 1;
if (process.argv[2]) {
  const b = parseInt(process.argv[2]);
  if (b) {
    while (c <= b) {
      a = a * c;
      c++;
    }
    console.log(a);
  }
} else { console.log(a); }
