#!/usr/bin/node

const cString = 'C is fun';
const x = parseInt(process.argv[2]);
let i = 0;

if (!isNaN(x)) {
  while (i < x) {
    console.log(cString);
    i++;
  }
} else if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
