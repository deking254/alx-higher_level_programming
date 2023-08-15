#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let n = 0;
  while (list[i]) {
    if (searchElement === list[i]) { n++; }
    i++;
  }
  return (n);
};
