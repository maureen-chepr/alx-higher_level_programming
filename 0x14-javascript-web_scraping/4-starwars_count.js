#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, function (error, response, body) {
  let moviesWithWedgeAntilles = 0;

  if (error) {
    console.log(error);
  }

  const filmsData = JSON.parse(body);
  for (let i = 0; filmsData.results[i] !== undefined; i++) {
    if (filmsData.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      moviesWithWedgeAntilles++;
    }
  }

  console.log(moviesWithWedgeAntilles);
});
