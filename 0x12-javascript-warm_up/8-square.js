#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);
let length = 0;

if (isNaN(squareSize)) {
  console.log('Missing size');
} else if (!isNaN(squareSize)) {
  while (length < squareSize) {
    console.log('X'.repeat(squareSize));
    length++;
  }
}
