#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (err, response, body) {
  if (response.statusCode === 200) {
    fs.writeFile(fileName, body, 'utf-8', function (err, data) {
      if (err) {
        return console.log(err);
      }
    });
  } else {
    console.log(err);
  }
});
