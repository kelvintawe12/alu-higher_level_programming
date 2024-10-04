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

  // Fetch each character's details in order
  let count = 0; // to track the number of requests made

  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);

      count++;
      // If this was the last character, we can exit the process
      if (count === characters.length) {
        process.exit();
      }
    });
  });
});
