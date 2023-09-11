// var name = "Sarah";
// const greeting = "Hello";
// console.log(greeting + " " + name);
// // Hello Sarah

// let age = 1;
// console.log("You're " + age);
// // You're 1

// 3. Только Constи Letявляются Блочными
// Область блока определяется фигурными скобками ( {}).

// function listFruits() {
//   if (true) {
//     const fruit1 = "orange"; //it exists in block scope
//     let fruit2 = "avocado"; //it exists in block scope
//     var fruit3 = "banana"; // it exists in function scope
//   }

//   console.log(fruit1);
//   console.log(fruit2);
//   console.log(fruit3);
// }

// listFruits();

// 4. Letи Varможно Переназначить, Но Constнельзя

// var name = "Sarah";
// const greeting = "Hello ";
// console.log(greeting + name);

// if we try to set the greeting again, we get an error

//greeting = "Hi";
// name = "Patience";
// console.log(greeting + name);

// let age = 1;
// console.log("You're " + age);

// age = 5; // we reset the age but no error
// console.log("You're " + age);
// function age(myAge) {

//   console.log The age of my Mom {myAge * 2}
// }
// age(26);

// function userInfo(userName, userAge) {
//   let result = "My name is " + userName + ", my age is " + userAge;
//   return result;
// }

// let girlInfo = userInfo("Sarah", 22);
// console.log(girlInfo); //My name is Sarah, my age is 22

// function userInfo(userName, userAge) {
//   if (userName === "Sarah") {
//     let result = "Hey " + userName;
//     return result;
//   } else {
//     return "You are not the right person";
//   }
// }

// let girlInfo = userInfo("Sah", 22);
// console.log(girlInfo); //Hey Sarah

// try {
//   //lines of code
// } catch (e) {
// } finally {
// }

// const func = () => {
//   try {
//     console.log("starting the try block");
//     hello;
//     console.log("finishing the try block");
//   } catch (err) {
//     //Check the type of error
//     if (err instanceof ReferenceError) {
//       console.log(`
//               Error Name : ${err.name},
//               Error Msg : ${err.message},
//               Error Stack : ${err.stack}`);
//     } else {
//       console.log("Other Error");
//     }
//   } finally {
//     console.log("Function done");
//   }
// };

// func();

// const func = (a, b) => {
//   let result;
//   try {
//     result = a / b;
//     if (b == 0) {
//       throw new Error("Cannot divide by Zero");
//     }
//   } catch (err) {
//     if (err instanceof ReferenceError) {
//       console.log(`
//               Error Name : ${err.name},
//               Error Msg : ${err.message}`);
//     } else {
//       console.log("Other Error");
//       console.log(`
//               Error Name : ${err.name},
//               Error Msg : ${err.message}`);
//     }
//   } finally {
//     console.log("Function done");
//   }
// };

// func(3, 0);
// let person = {
//   firstName: "Sarah",
//   eyeColor: "blue",
//   eat: function () {
//     console.log("I love chocolate");
//   },
// };
// person.eat();

// let text = document.getElementById("one").innerHTML;
// alert("The first heading is " + text); //output : "The first heading is Welcome"
// const myList = document.querySelector("ul");
// console.log(myList.firstElementChild);
// myList.firstElementChild.innerText = "BANANA";
// console.log(myList.parentElement);

var number = 5;
alert(number);

let num = 10
num = 7;

const pi = 3.14;
pi = 5;
console.log(const);
weqw 