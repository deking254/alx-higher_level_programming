#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
let k = 0;
let i, films, j;
req.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(response.body);
    films = res.results;
    const person = 'https://swapi-api.alx-tools.com/api/people/films/18/';
    for (i in films) {
      const film = films[i];
      for (j in film.characters) {
        const character = film.characters[j];
        if (character === person) {
          k = k + 1;
        }
      }
    }
    console.log(k);
  }
});
