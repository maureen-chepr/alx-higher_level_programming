#!/usr/bin/node
const request = require('request');
const movieApi = 'http://swapi.co/api/films/';

request.get(movieApi + process.argv[2], function (errorMovie, responseMovie, bodyMovie) {
  if (errorMovie) throw errorMovie;
  if (responseMovie.statusCode === 200) {
    const movieData = JSON.parse(bodyMovie);
    const characterPromises = [];

    for (const characterUrl of movieData.characters) {
      characterPromises.push(new Promise(function (resolve, reject) {
        request.get(characterUrl, function (errorCharacter, responseCharacter, bodyCharacter) {
          if (errorCharacter) throw errorCharacter;
          if (responseCharacter.statusCode === 200) {
            resolve(JSON.parse(bodyCharacter).name);
          } else {
            reject(Error('Unknown'));
          }
        });
      }));
    }

    Promise.all(characterPromises).then(function (characterNames) {
      characterNames.forEach(function (name) {
        console.log(name);
      });
    });
  }
});
