#!/usr/bin/node

const request = require('request');
const MovieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + MovieId;
request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
