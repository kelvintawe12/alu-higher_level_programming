#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (this._isValid(w) && this._isValid(h)) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  _isValid(value) {
    return Number.isInteger(value) && value > 0;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
