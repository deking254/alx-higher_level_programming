#!/usr/bin/node
const req = require('request');
const util = require('util');
const requestPromise = util.promisify(req);
const id = process.argv[2];
let characters, i;

async function makeGetRequest (url) {
  try {
    const response = await requestPromise(url);
    if (response.statusCode !== 200) {
      throw new Error(`HTTP Status Code: ${response.statusCode}`);
    }
    const responseBody = response.body;
    return responseBody;
  } catch (error) {

  }
}
const movies = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';

req.get(movies, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    characters = JSON.parse(data.body).characters;
    for (i in characters) {
      makeGetRequest(characters[i]).then((result) => {
        console.log(JSON.parse(result).name);
      });
    }
  }
});
/*
    characters = JSON.parse(data.body).characters;
    for (i in characters) {
      fetch(characters[i]).then((data) => {
          person = JSON.parse(data.body).name;
          name.push("person");
        });
      };
    }
}); */
