#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
let characters;
const movies = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';

req.get(movies, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    characters = JSON.parse(body).characters;
    print(characters, 0);
  }
});

function print (characters, index) {
  req.get(characters[index], (error, res, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      index = index + 1;
      if (index < characters.length) {
        print(characters, index);
      }
    }
  });
}
