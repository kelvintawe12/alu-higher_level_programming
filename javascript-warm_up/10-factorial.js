#!/usr/bin/node

// Define the factorial function
function factorial (n) {
  if (isNaN(n) || n < 0) return 1;
  if (n === 0) return 1;
  return n * factorial(n - 1);
}

// Convert the argument to an integer
const arg = parseInt(process.argv[2], 10);

// Print the factorial of the argument
console.log(factorial(arg));
