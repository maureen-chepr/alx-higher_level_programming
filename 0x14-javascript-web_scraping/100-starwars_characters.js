#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi.co/api/films/';
const movieId = process.argv[2];

request.get(apiUrl + movieId, function (errorMovie, responseMovie, bodyMovie) {
  if (errorMovie) throw errorMovie;
  else if (responseMovie.statusCode === 200) {
    const movieData = JSON.parse(bodyMovie);
    for (let characterUrl of movieData.characters) {
      request.get(characterUrl, function (errorCharacter, responseCharacter, bodyCharacter) {
        if (errorCharacter) throw errorCharacter;
        else if (responseCharacter.statusCode === 200) {
          const characterData = JSON.parse(bodyCharacter);
          console.log(characterData.name);
        }
      });
    }
  }
});
