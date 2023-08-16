// //Console logs

// console.log("content to display");
// console.log("Line2");

// //Variables
// let x = 3;
// let X = 5;
// let my_name = "Alexander";
// let my_name2 = "Meshkov";
// console.log(x + X);

// //CamelCase

// let myName = "Alexander";
// let thisIsMyName = "Alex";

// //Undefined

// // let 1a; // cannot start with a digit
// // let my-name; // hyphens '-' aren't allowed in the name
// // console.log(a);

// //Keywords
// //let keyword tells the browser to create variables:

// let z, y;
// z = 5 + 6;
// y = z * 10;

// //DataTypes
// //Strings
// let exampleString = "Hello";
// let exampleString2 = "World";
// console.log(exampleString + exampleString2);

// console.log("2");
// console.log(2);

// //Длинные Литеральные Строки

// let longString =
//   "This is a very long string which needs " +
//   "to wrap across multiple lines because " +
//   "otherwise, my code is unreadable.";

// console.log(longString);

// //Символ обратной косой черты\
// //В конце каждой строки, чтобы указать, что строка будет продолжена на следующей строке.
// //Убедитесь, что после обратной косой черты нет пробела или любого другого символа.
// let longString2 =
//   "This is a very long string which needs \
// to wrap across multiple lines because \
// otherwise my code is unreadable.";

// let lengthTxt = longString.length;
// console.log(lengthTxt);

// // Метод indexOf(): возвращает индекс (положение) первого вхождения указанного текста в строку:
// // Возвращает -1, если текст не найден

// let str1 = "Hello Everyone, please say hello to the class";
// let posUppercaseHello = str1.indexOf("Hello"); // case sensitive
// let posLowercaseHello = str1.indexOf("hello");
// console.log(posUppercaseHello); // 0
// console.log(posLowercaseHello); // 27

// let secondstr = "hello Everyone, please say hello to the class";
// let secondStrPosHello = secondstr.indexOf("hello");
// console.log(secondStrPosHello); // 0

// //indexOf()
// console.log(myName.indexOf("x"));

// //Методы substring(startIndex, endIndex):
// console.log(myName.substring(0, 4));
// let str = "Hello Everyone, please say hello to the class ";
// str.substring(0, 4); //returns "Hell" --> the index 4 isn't included
// str.substring(2, 4); //returns "ll"
// str.substring(15); //returns "please say hello to the class"

// //toLowerCase(): возвращает строку, все символы которой преобразованы в нижний регистр.

// let myStr = "wwssrgIBVbkbuibUVubUBUbVYvVuibkuBubv ";
// myStr.toLowerCase();
// //returns "hello everyone, please say hello to the class "

// //Numbers

// console.log(5 + 3);
// console.log(5 - 3);
// console.log(5 / 3);

// //Числовые Методы
// // Метод isNaN(x): вернуть true или false
// let op = "me";
// isNaN(op); //returns true because op is Not a Number

// // Метод toString(): возвращает число в виде строки.
// let op2 = 10;
// op2.toString(); //returns "10"
// console.log(op2);

// // Метод toFixed(): возвращает строку с числом, записанным с указанным количеством знаков после запятой:
// let op3 = 10.6789;
// op3.toFixed(0); // returns 11
// op3.toFixed(2); // returns 10.68.
// console.log(op3.toFixed(1));

// //Comparison
// let q = 1;
// //Checks value - Regardless of type
// console.log(q === 1); //true
// //Checks type and value
// console.log(q === "1"); //false because q - String

// //          /!=	Not equal
// //           >	Greater than
// //           >=	Greater than or equal to
// //            <	Less than
// //           <=	Less than or equal to
// //           ||	Or
// //           &&	And
// //           /!	Not (if x is true, then x! is false)
// let u = 6;
// console.log(u > 5 || u === 2);

// //User Interface Functions
// console.log("Befora alert");
// alert(" Welcome to my website");
// console.log("After Alert");

// //Prompt - Подсказка
// let age = prompt("How old are you?", 20);
// alert(`You are ${age} years old!`); // You are 20 years old!

// let userAnswer = prompt("What is your name?", "Guest");
// console.log("Welcome to my website" + userAnswer);

// . Подтвердить
// Функция confirm показывает модальное окно с вопросом и двумя кнопками: ОК и Отмена.
// Результат - trueесли нажата ОК и false иначе.

// confirm(question)

// let isBoss = confirm("Are you boss");
// alert(isBoss);

// Javascript Arrays
// Массивы — это особый тип объектов. Оператор typeof()в JavaScript возвращает «объект» для массивов.
// let users = ["John", "Bill", "Nancy"];
// console.log(typeof users); // object
// Доступ К Элементам В Массиве
// console.log(users[1]);
// let colors = ["blue", "yellow", "green", 54];
// let favorite = colors[0];
// let secondFavorite = colors[3];
// console.log(favorite); // blue
// console.log(secondFavorite); // green

// let sampleArray = [
//   [1, 2, 5],
//   [7, 6, 10, 11, 12],
//   [13, 12, 16, 32],
// ];
// console.log(sampleArray[0][1]);
// console.log(sampleArray[2][2]);

// Изменение Элемента Массива

// let colors = ["blue", "yellow", "green"];
// colors[5] = "pink";
// console.log(colors); // ["pink", "yellow", "green"];

// Свойства Массива
// Свойство length: возвращает длину массива (количество элементов внутри массива).
// Счет lengthначинается с 1 (а не с 0 , как индекс (т.е. видно выше))

// let colors = ["blue", "yellow", "green"];
// arrayLenght = colors.length; // 3
// console.log(arrayLenght);

//Методы Массива
//Метод push(): добавляет новый элемент в конец массива

let colors = ["blue", "yellow", "green"];
colors.push("orange");
console.log(colors); // ["blue", "yellow", "green", "orange"];

//Метод pop(): удаляет последний элемент из массива:
// colors.pop();
// colors.pop();
// colors.pop();
// colors.pop();
// console.log(colors); //["blue", "yellow"];

//Метод splice(): добавляет новые элементы в массив/удаляет элементы

// colors.splice(1, 1, "Redd", "Purple", 45, 23, 455);
// console.log(colors); //  ["blue", 45, 23, "green"];

// Метод slice(): нарезает часть массива и начинает новый массив.
// Метод slice()создает новый массив. Он не удаляет никаких элементов из исходного массива .
// Затем метод выбирает элементы от начального аргумента до (но не включая) конечного аргумента.
// let colors = ["blue", "yellow", "green", "pink"];
// let favorite = colors.slice(2);
// console.log(favorite); // ["green" , "pink"];
// console.log(colors); // ["blue", "yellow", "green", "pink" ];

// let secondFavorite = colors.slice(0, 1);
// console.log(secondFavorite); //[ 'blue' ]
// console.log(colors); // ["blue", "yellow", "green", "pink" ];

//Objects
// let person = {
//   firstName: "Alex",
//   lastname: "Meshkov",
//   age: 31,
//   eyeColor: "green",
// };
// console.log(person.firstName);
// console.log(person["firstName"]);

// Adding/ Changing Object Properties

// Conditional JS

// let x = 20;

// if (x >= 21) {
//   console.log("You can drink in the united states");
// }
// let age = 2;

// if (age > 18) {
//   console.log("We can go to a pub together !!");
// } else {
//   console.log("Sorry...You have to stay at home tonight");
// }
// let age = 2;

// if (age === 18) {
//   console.log("It's your birthday !!");
// } else if (age > 18) {
//   console.log("We can go to a pub together !!!");
// } else {
//   console.log("Sorry...You have to stay at home tonight");
// }

// exercise
// let userAnswer = prompt("What is your age?");
// console.log(userAnswer);
// if (userAnswer == 18) {
//   alert("Mazal tov you can drive");
// } else if (userAnswer > 18) {
//   alert("You are over 18 you can drive");
// } else {
//   alert("You are sooo young");
// }

// SWITCH CASE
// let fruit = "Papayas";

// switch (fruit) {
//   case "Oranges":
//     console.log("Oranges are $0.59 a pound.");
//     break;
//   case "Mangoes":
//   case "Papayas":
//     console.log("Mangoes and papayas are $2.79 a pound.");
//     // expected output: "Mangoes and papayas are $2.79 a pound."
//     break;
//   default:
//     console.log("Sorry, we are out of " + fruit + ".");
// }
// Loops
// for (let i = 0; i < 5; i++) {
//   console.log("the current number is " + i);
// }
// for (let i = 0; i <= 10; i++) {
//   console.log(i);
// }
// let arr = ["red", "green", "blue", "purple", "grey"];
// for (let i = 0; i < arr.length; i++) {
//   console.log(arr[i]);
// }

// let oddArray;
// for (let i = 0; i < 15; i++) {
//   console.log("the current number is " + i);
// }

// Break Statement

for (let i = 0; i < 10; i++) {
  if (i === 3) {
    break;
  }
  console.log("The number is " + i); // 0 1 2
}
