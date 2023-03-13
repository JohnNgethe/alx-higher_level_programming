#!/usr/bin/node

function factorial (n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
if (isNaN(process.argv[2])) console.log(1);
else {
  const answer = factorial(Number(process.argv[2]));
  console.log(answer);
}
