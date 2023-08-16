// Exercise 1
const people = ["Greg", "Mary", "Devon", "James"];
// Part I - Review About Arrays
// 1.
people.splice(0, 1);
console.log(people);
// 2.
people.splice(2, 2, "Jason");
console.log(people);
// 3.
people.push("Alexander");
console.log(people);
// 4.
let func = people.indexOf("Mary");
console.log(func);
// 5.
let newArr = people.slice(0, 3);
console.log(newArr);
