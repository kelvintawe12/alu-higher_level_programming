#!/usr/bin/node

const { dict } = require('./101-data.js');

const occurrences = {};

for (const [userId, count] of Object.entries(dict)) {
  if (!occurrences[count]) {
    occurrences[count] = [];
  }
  occurrences[count].push(userId.toString());
}

console.log(occurrences);
