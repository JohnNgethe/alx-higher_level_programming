#!/usr/bin/node
const max = 0;
if (process.argv.length === 2) console.log(max);
else if (process.argv.length === 3) console.log(max);
else {
  const sort = [];
  process.argv.forEach((item, index) => {
    sort.push(Number(item));
  });
  sort.sort((a, b) => a - b);
  console.log(sort[sort.length - 2]);
}
