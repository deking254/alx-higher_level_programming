#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
let todos, i;
req.get(url, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    todos = JSON.parse(data.body);
    const n = {};
    for (i in todos) {
      if (todos[i].completed) {
        const property = String(todos[i].userId);
        if (n[property]) {
          n[property] = n[property] + 1;
        } else {
          n[property] = 1;
        }
      }
    }
    console.log(n);
  }
});
