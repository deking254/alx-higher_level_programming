#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const Filename = args[2];
const data = args[3];
fs.writeFile(Filename, data, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
