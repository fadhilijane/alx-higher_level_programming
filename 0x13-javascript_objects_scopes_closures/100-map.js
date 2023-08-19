#!/usr/bin/node

const List = require('./100-data.js').list;
console.log(List);
console.log(List.map((item, index) => item * index));
