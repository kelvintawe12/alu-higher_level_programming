#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value += 1;
  }
};

console.log(myObject);

// Call the incr method and log the object
myObject.incr();
console.log(myObject);

// Call the incr method again and log the object
myObject.incr();
console.log(myObject);

// Call the incr method one more time and log the object
myObject.incr();
console.log(myObject);
