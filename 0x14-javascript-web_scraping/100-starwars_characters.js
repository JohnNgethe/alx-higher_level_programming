#!/usr/bin/node

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(function (element) {
      request(element, function (error, response, body) {
        if (error) {
          return console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
