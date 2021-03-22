#!/usr/bin/node
/*
  prints a factorial with factorial function
  1st argument is int used for computing the factorial
*/

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

const args = process.argv;
console.log(factorial(parseInt(args[2])));
