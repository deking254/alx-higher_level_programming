#!/usr/bin/node
let i = 0;
while (process.argv[i]) {
  if (i === 2) {
    console.log(process.argv[i]);
  }
  i += 1;
}
if (i === 2) {
  console.log('No argument');
}
