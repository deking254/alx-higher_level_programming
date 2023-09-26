#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
let res;
const Filename = args[3];
req.get(url, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    res = data.body;
    fs.writeFile(Filename, res, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
