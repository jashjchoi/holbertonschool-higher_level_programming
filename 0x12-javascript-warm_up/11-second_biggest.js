#!/usr/bin/node
/*
  searches the second biggest integer in the list of arguments
*/

const list = process.argv;
list.splice(0, 2);

if (list.length < 2) {
  console.log(0);
} else {
  list.sort((a, b) => b - a);
  console.log(list[list.length - 2]);
}
