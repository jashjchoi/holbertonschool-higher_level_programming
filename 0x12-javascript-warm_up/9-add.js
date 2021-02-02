#!/usr/bin/node
/*
  prints the addition of 2 integers
  with this prototype: function add(a, b)
*/

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const num = process.argv;

console.log(add(num[2], num[3]));
