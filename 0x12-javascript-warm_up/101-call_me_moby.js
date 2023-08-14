#!/usr/bin/node
let i = 0;

function theFunction (a, b) {
  while (i < a) {
    b();
    i++;
  }
}
module.exports = { callMeMoby: theFunction };
