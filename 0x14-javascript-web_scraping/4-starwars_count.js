#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const result = JSON.parse(body).results.filter((movie) => {
    return movie.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(result);
});
