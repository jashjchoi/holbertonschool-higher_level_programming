#!/usr/bin/node
/*
  increments and calls a function. must be visible from outside
  Prototype: function (number, theFunction)
*/

exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  return theFunction(number);
};
