#!/usr/bin/node
const dct = require('./101-data').dict;
const newish = {};
let key = '';
for (key in dct) {
  newish[dct[key]] = [];
}
for (key in dct) {
  newish[dct[key]].push(key);
}
console.log(newish);
