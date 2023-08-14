#!/usr/bin/node
function factorio (b) {
  let a = 1;
  let c = 1;
  while (c <= b) {
    a = a * c;
    c++;
  }
  console.log(a);
}
if (process.argv[2]) {
  const e = parseInt(process.argv[2]);
  if (e) { factorio(e); }
} else { console.log(a); }
