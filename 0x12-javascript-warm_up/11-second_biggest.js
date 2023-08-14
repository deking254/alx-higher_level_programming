#!/usr/bin/node
let i = 0;
let a = 0;
let b = 0;
let n = 0;
let stati = 0;
if (process.argv.length > 3)
{
while (process.argv[i])
{
while (process.argv[n])
{
a = parseInt(process.argv[i]);
b = parseInt(process.argv[n]);
if (typeof(a) == "number"  && typeof(b) == "number")
{
if (a < b)
stati += 1;
}
n++;
}
if (stati == 1)
console.log(process.argv[i]);
stati = 0;
n = 0;
i++;
}
}
else
console.log(0);
