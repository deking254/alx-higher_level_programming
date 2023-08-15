#!/usr/bin/node
const lst = require('./100-data').list;
class Logg {
  constructor () {
    this.n = -1;
  }
}
const lo = new Logg();
if (lst) {
  console.log(lst);
  console.log(lst.map(function multi (item) {
    if (lo) {
      lo.n++;
      return (item * lo.n);
    }
  }));
}
