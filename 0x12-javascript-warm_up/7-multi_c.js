#!/usr/bin/node
let a = 0;
let b = parseInt(process.argv[2]);
if (b)
{
if (b > 0)
{
while (a < b)
{
console.log("C is fun");
a += 1;
}
}
}
else if (b != 0)
console.log("Missing number of occurrences");
