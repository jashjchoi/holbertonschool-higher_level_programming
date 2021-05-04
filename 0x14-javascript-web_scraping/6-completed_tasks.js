#!/usr/bin/node
// computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonBody = JSON.parse(body);
    const dictCompletTodoUser = {};
    for (const todo of jsonBody) {
      if (todo.completed) {
        if (dictCompletTodoUser[todo.userId]) {
          dictCompletTodoUser[todo.userId] += 1;
        } else {
          dictCompletTodoUser[todo.userId] = 1;
        }
      }
    }
    console.log(dictCompletTodoUser);
  }
});
