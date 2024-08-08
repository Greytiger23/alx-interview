#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  const printCharacterName = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printCharacterName(index + 1);
    });
  };
  printCharacterName(0);
});
