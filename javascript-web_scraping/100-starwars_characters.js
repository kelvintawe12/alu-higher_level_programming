#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters || [];

  // Fetch each character's details
  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
