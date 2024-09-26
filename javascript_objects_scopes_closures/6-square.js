#!/usr/bin/node

const Square = require('./5-square');

class SquareWithChar extends Square {
  charPrint (c) {
    const character = c || 'X'; // Use 'X' if no character is provided
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = SquareWithChar;
