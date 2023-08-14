#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const newArr = process.argv.slice(2).map(Number);
  const maxToMin = newArr.sort(function (a, b) { return b - a; });
  const secMax = maxToMin[1];
  console.log(secMax);
}
