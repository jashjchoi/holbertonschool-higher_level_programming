#!/usr/bin/node
// prints the title of a Star Wars movie
// where the episode number matches a given int
const request = require('request');
const movieID = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/';
const requestURL = url + movieID;

request(requestURL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  }
});
