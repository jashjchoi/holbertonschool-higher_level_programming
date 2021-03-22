#!/usr/bin/node
/*
  print x times with loop function
*/
const args = process.argv;

if (!args[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let x = args[2]; x > 0; x--) {
    console.log('C is fun');
  }
}
