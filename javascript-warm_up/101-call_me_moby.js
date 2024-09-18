#!/usr/bin/node

// Define the function that executes `theFunction` x times
function callMeMoby(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the function to make it available outside
exports.callMeMoby = callMeMoby;
