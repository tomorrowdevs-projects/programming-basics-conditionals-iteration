/*
In this exercise you will create a program that: 
- reads a letter of the alphabet from the user.   
- If the user enters **a, e, i, o or u** then your program should display a message indicating that the entered letter is a **vowel**.  
- If the user enters **y** then your program should display a message indicating that **sometimes y is a vowel, and sometimes y is a consonant**.   
- Otherwise, your program should display a message indicating that **the letter is a consonant**.
*/

const prompt = require('prompt-sync')({sigint: true}); // Added the node module to be able to call the prompt function

// Asking the user an input until it is not a one digit letter
let letter;
do {
letter = prompt("Inserisci una lettera dell'alfabeto: ");
} while (isNaN(Number(letter)) != true || letter.length != 1);

// Using th switch constructor to avoid of using a chain of If,else IF, statements
switch (letter) {
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
    case "A":
    case "E":
    case "I":
    case "O":
    case "U":
        console.log("La lettera inserita è una vocale.");
    break;

    case "y":
    case "Y":
        console.log("La lettera inserita è una vocale e talvolta una consonante.");
    break;
    
    default:
        console.log("La lettera inserita è una consonante.");
}
