#!/usr/bin/node
const listt = require('./100-data.js').listt;
console.log(listt);
console.log(listt.map((item, index) => item * index));
