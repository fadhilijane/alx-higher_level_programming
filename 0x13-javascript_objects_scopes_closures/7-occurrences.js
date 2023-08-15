#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let count = 0;

  while (i < list.length) {
    if (searchElement === list[i]) {
      count++;
    }
    i++;
  }
  return count;
};
