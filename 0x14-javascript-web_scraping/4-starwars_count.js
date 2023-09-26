#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
let k = 0;
let i, films, j;
const person = 'https://swapi-api.alx-tools.com/api/people/18/';
req.get(id, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(response.body);
    films = res.results;
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
