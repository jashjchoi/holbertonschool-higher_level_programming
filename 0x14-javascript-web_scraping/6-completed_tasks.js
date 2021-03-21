#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (response.statusCode === 200) {
    const todosFile = JSON.parse(body);
    const completedList = {};
    for (const todo of todosFile) {
      if (todo.completed) {
        if (completedList[todo.userId]) {
          completedList[todo.userId] += 1;
        } else {
          completedList[todo.userId] = 1;
        }
      }
    }
    console.log(completedList);
  } else {
    console.log(err);
  }
});
