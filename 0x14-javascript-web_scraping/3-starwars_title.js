#!/usr/bin/node
const request = require('request');
const index = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${index}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
