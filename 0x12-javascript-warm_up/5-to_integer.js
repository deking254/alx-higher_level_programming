#!/usr/bin/node
let a = parseInt(process.argv[2]);
if (a)
{
console.log("My number: ".concat(a));
}
else
console.log("Not a number");
