#!/usr/bin/node
if (isNaN(process.argv[2])) console.log('Missing size');
const num = Number(process.argv[2]);
for (let i = 0; i < num; i++) {
  for (let j = 0; j < num; j++) {
    process.stdout.write('X');
  }
  console.log('');
}
