#!/usr/bin/node
let a = process.argv[2];
let b = process.argv[3];
if (a === undefined) {
  a = 'undefined';
}
if (b === undefined) {
  b = 'undefined';
}
console.log(a.concat(' is ').concat(b));
