#!/usr/bin/node
// imports an array and computes a new array
// A new list must be created with each value equal to the value of the initial list
// multipled by the index in the list

const list = require('./100-data.js').list;

const nList = list.map((x, y) => x * y);
console.log(list);
console.log(nList);
