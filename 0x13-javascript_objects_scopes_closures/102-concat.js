#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) { return; }
  fs.writeFile(process.argv[4], data, 'utf8', (err) => {
    if (err) { console.log('Error'); }
  });
});
fs.readFile(process.argv[3], 'utf8', (err, dat) => {
  if (err) { return; }
  fs.appendFile(process.argv[4], dat, 'utf8', (err) => {
    if (err) { console.log('Error'); }
  });
});
