#!/usr/bin/node
// file system module
const fs = require('fs');
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, function (err, dataA) {
  if (err) throw err;
  fs.readFile(fileB, function (err, dataB) {
    if (err) throw err;
    fs.writeFile(fileC, dataA + dataB, function (err) {
      if (err) throw err;
    });
  });
});
