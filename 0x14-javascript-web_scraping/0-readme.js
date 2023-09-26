#!/usr/bin/node
const Filename = process.argv[2];
const f = require('fs');
f.readFile(Filename, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
