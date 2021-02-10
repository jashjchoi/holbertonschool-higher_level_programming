#!/usr/bin/node
// prints the number of movies where the character
// “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];
let counter = 0;

request(url, function (err, response, body) {
  if (err) {
    console.log('code:', response.statusCode);
  } else {
    const jsonFile = JSON.parse(body);
    for (const film of jsonFile.results) {
      for (const character of film.characters) {
        if (character.includes('18')) { counter += 1; }
      }
    }
  }
  console.log(counter);
});
