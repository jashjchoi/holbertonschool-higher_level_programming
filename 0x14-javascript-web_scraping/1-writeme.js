#!/usr/bin/node
// reads and prints the content of a file
const fs = require('fs');
const fileName = process.argv[2];
const text = process.argv[3];

fs.writeFile(fileName, text, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
