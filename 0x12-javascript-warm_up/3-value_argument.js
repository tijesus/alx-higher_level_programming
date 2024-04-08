#!/usr/bin/node

// console.log(process.argv[2] ? process.argv[2] : 'No argument');

const argv = process.argv[2];
if (argv  === undefined) {
  console.log('No argument');
}
else {
  console.log(argv);
}
