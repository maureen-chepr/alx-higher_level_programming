#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const filmsData = JSON.parse(body);
    let count = 0;

    for (const film of filmsData.results) {
      if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    }

    console.log(count);
  }
});
