#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body).reduce((acc, todo) => {
    if (!acc[todo.userId]) {
      if (todo.completed) {
        acc[todo.userId] = 1;
      }
    } else {
      if (todo.completed) {
        acc[todo.userId] += 1;
      }
    }
    return acc;
  }, {});
  console.log(dict);
});
