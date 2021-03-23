#!/usr/bin/node
/*
  searches the second biggest integer in the list of arguments
*/

if (!process.argv[2] || !process.argv[3] || process.argv[1] === 1) {
  console.log('0');
} else {
  const list = [];
  for (let i = 0; process.argv[i]; i++) {
    list.push(process.argv[i]);
  }
  list.sort();
  const index = list.length - 2;
  console.log(list[index]);
}
