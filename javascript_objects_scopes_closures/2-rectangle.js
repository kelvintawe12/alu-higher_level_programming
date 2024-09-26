#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (this._isValid(w) && this._isValid(h)) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object
      return {};
    }
  }

  _isValid(value) {
    return Number.isInteger(value) && value > 0;
  }
}

module.exports = Rectangle;
