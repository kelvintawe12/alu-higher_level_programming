#!/usr/bin/node

let count = 0; // Initialize a counter

exports.logMe = function (item) {
  console.log(`${count}: ${item}`); // Print the current count and the item
  count++; // Increment the counter
};
