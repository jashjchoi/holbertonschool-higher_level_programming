#!/usr/bin/node
/*
  searches the second biggest integer in the list of arguments
*/

if (!process.argv[2] || !process.argv[3])
{
  console.log('0');
} else {
    let list = [];
    for (let i = 0; process.argv[i]; i++) {
        list.push(process.argv[i]);
    }
  list.sort();
    let index = list.length - 2;
    console.log(list[index]);
}
