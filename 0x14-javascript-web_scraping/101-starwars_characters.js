#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
let characters, i, person;
const movies = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';
req.get(movies, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    characters = JSON.parse(data.body).characters;
    for (i in characters) {
      req.get(characters[i], (error, data) => {
        if (error) {
          console.log(error);
        } else {
          person = JSON.parse(data.body).name;
          console.log(person);
        }
      });
    }
  }
});
