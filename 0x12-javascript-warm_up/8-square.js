#!/usr/bin/node
/*
  print square with loop function
*/
const num = parseInt(process.argv[2]);

if (!num) {
  console.log('Missing size');
} else if (num < 0) {
  console.log('');
} else {
  for (let x = 0; x < num; x++) {
    console.log('X'.repeat(num));
  }
}
