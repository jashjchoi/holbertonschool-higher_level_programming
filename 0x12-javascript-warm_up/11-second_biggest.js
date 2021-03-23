#!/usr/bin/node
/*
  searches the second biggest integer in the list of arguments
*/

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const idx = process.argv.slice(2);
  idx.sort(function (a, b) { return b - a; });
  console.log(idx[1]);
}
