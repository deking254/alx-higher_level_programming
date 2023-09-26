#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
req.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(response.body);
    console.log(res.title);
  }
});
