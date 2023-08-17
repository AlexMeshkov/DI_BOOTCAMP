// Exercise 1
// const people = ["Greg", "Mary", "Devon", "James"];
// Part I - Review About Arrays
// 1.
// people.splice(0, 1);
// console.log(people);
// 2.
// people.splice(2, 2, "Jason");
// console.log(people);
// 3.
// people.push("Alexander");
// console.log(people);
// 4.
// let func = people.indexOf("Mary");
// console.log(func);
// 5.
// let newArr = people.slice(1, 3);
// console.log(newArr);
// 6.
// console.log(people.indexOf("Foo"));
// The use of -1 is because the indexOf operation will return -1 in the event the searched for value does not exist in the array.
// 7.
// let last = people.length;
// console.log(last);
// Part II - Loops
// 1
// for (let i = 0; i < last; i++) {
//   console.log(people[i]);
// }
// 2
// for (let i = 0; i < people.length; i++) {
//   console.log(people[i]);
//   if (people[i] == "Devon") {
//     break;
//   }
// }
// Exercise 2

// colors = ['Black', 'Green', 'Orange', 'Beige', 'Purple'];
// prefixes = ['st', 'nd', 'rd', 'th', 'th'];

// for (i = 0; i < colors.length; i++) {
//     console.log("My " +(i+1) + prefixes[i] + " choice is " + colors[i]);
// }

//  Exercise 3

// let number = prompt("Write a number");
// console.log(typeof (number));

// let number2 = 0;
// do {
//     number2 = prompt("Write a number (exit loop if number >= 10)");
//     console.log(number2);
// } while (number2 < 10);

//  Exercise 4

// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }

// console.log("Number of floors " + building.numberOfFloors);
// console.log("Number of apts on 1st floor " + building.numberOfAptByFloor.firstFloor);
// console.log("Number of apts on 3rd floor " + building.numberOfAptByFloor.thirdFloor);
// console.log("Second tenant " + building.nameOfTenants[1] + " number of rooms " + building.numberOfRoomsAndRent.dan[0]);

// if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]) {
//     building.numberOfRoomsAndRent.dan[1] = 1200;
// }
// console.log(building.numberOfRoomsAndRent.dan[1]);

// Exercise 5

// const family = {
//     dad: 'Gillian',
//     mum: 'Dana',
//     daughter: 'Jill'
// }

// for (let key in family) {
//     console.log(key);
// }

// for (let key in family) {
//     console.log(family[key]);
// }

// Exercise 6

// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   }
// let result = "";
//   for (let key in details) {
//     result += key + " " + details[key] + " ";
//   }
// console.log(result)

// Exercise 7

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
let result = "";
for (let i = 0; i < names.length; i++) {
  result += names[i][0];
}
console.log(result);
