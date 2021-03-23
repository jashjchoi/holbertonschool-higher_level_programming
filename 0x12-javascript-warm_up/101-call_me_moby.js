#!/usr/bin/node
/*
  executes x times a function. must be visible from outside
  Prototype: function (x, theFunction)
*/
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
