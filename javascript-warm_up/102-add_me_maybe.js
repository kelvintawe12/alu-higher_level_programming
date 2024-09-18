#!/usr/bin/node

// Define the function that increments `number` and calls `theFunction`
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

// Export the function to make it available outside
exports.addMeMaybe = addMeMaybe;
