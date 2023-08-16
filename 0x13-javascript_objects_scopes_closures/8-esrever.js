#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const last = list.length - 1;

  for (let i = last; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList);
};
