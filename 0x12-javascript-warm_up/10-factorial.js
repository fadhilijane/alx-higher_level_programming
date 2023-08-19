#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

console.log(factorial(Number(process.argv[2])));
