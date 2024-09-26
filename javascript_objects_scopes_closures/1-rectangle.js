#!/usr/bin/node

function Rectangle(w, h) {
  if (this._isValid(w) && this._isValid(h)) {
    this.width = w;
    this.height = h;
  } else {
    this.width = undefined;
    this.height = undefined;
  }
}

Rectangle.prototype._isValid = function (value) {
  return Number.isInteger(value) && value > 0;
};

module.exports = Rectangle;
