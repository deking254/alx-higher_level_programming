#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
let k = 0;
let i, films, j, res;
const person = 'https://swapi-api.alx-tools.com/api/people/18/';
if (id) {
  req.get(id, (error, response) => {
    if (error) {
      console.log(error);
    } else {
      try {
        res = JSON.parse(response.body);
      } catch (error) {
        return;
      }
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
}
