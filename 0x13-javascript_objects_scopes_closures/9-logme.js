#!/usr/bin/node
class Log {
  constructor () {
    this.n = 0;
  }
}
const logg = new Log();
exports.logMe = function (item) {
  if (logg) {
    logg.n++;
    console.log('%d: %s', logg.n, item);
  }
};
