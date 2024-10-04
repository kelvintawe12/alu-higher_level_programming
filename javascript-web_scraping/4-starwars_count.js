#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const movies = data.results || [];
  let count = 0;

  // Full URL for Wedge Antilles
  const wedgeAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

  movies.forEach(movie => {
    // Check if the character URL exists in the movie's characters array
    if (movie.characters.includes(wedgeAntillesUrl)) {
      count++;
    }
  });

  console.log(count);
});
