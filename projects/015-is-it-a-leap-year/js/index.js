/*
The rules for determining whether a year is a leap year follow:  
- Any year that is divisible by 400 is a leap year.
- Of the remaining years, any year that is divisible by 100 is not a leap year. 
- Of the remaining years, any year that is divisible by 4 is a leap year.
- All other years are not leap years.  

Write a program that **reads a year** from the user and 
displays a message indicating **whether it is a leap year**.

Example:  
Input: 2024  
Output: Leap year
*/

const prompt = require('prompt-sync')({sigint: true});

let year;
do {
    year = prompt("Inserisci un anno: => ");
} while (Number.isInteger(Number(year)) != true || Number(year) < 0 || isNaN(year) == true);

((year % 4) == 0 || (year % 400) == 0) ? console.log(year + " è un anno bisestile!"): console.log(year + " non è un anno bisestile!");

/*
switch ((year % 4) == 0 || (year % 400) == 0) {
    case true:
        console.log(year + " è un anno bisestile!");
    break;
    default:
        console.log(year + " non è un anno bisestile!");
}
*/