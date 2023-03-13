#!/usr/bin/node
const number = parseInt(process.argv[2]);

if (number) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
