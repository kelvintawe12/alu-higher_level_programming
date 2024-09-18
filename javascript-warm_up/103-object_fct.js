#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value += 1;
  }
};

// Override the toString method to customize the function representation
myObject.incr.toString = function () {
  return '[Function (anonymous)]';
};

console.log({
  type: myObject.type,
  value: myObject.value
});

myObject.incr();
console.log({
  type: myObject.type,
  value: myObject.value,
  incr: myObject.incr
});

myObject.incr();
console.log({
  type: myObject.type,
  value: myObject.value,
  incr: myObject.incr
});

myObject.incr();
console.log({
  type: myObject.type,
  value: myObject.value,
  incr: myObject.incr
});
