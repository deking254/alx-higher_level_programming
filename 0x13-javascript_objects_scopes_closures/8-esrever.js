#!/usr/bin/node
exports.esrever = function (list) {
  const length = list.length;
  let start = 0;
  let end = length - 1;
  if (length % 2) {
    while ((end !== start)) {
      const a = list[start];
      const b = list[end];
      list[start] = b;
      list[end] = a;
      start++;
      end--;
    }
  } else {
    while ((end - start) !== 1) {
      const a = list[start];
      const b = list[end];
      list[start] = b;
      list[end] = a;
      start++;
      end--;
    }
  }
  return (list);
};
