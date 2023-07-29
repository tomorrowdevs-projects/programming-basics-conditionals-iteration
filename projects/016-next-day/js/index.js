/*
Write a program that **reads a date** from the user and **computes its immediate successor**.   
The date will be **entered in numeric form with three separate input statements**: 
- year   
- month
- day


Example:    
- if the user enters values that represent 2019-11-18 the next day is 2019-11-19.  
- If the user enters values that represent 2019-11-30 the next day is 2019-12-01. 
- If the user enters values that represent 2019-12-31 the next day is 2020-01-01. 


Ensure that your program **works correctly for leap years**.
*/

const prompt = require('prompt-sync')({sigint: true});

let year = Number(prompt("Inserire anno: => "));
let month = Number(prompt("Inserire mese: => "));
let day = Number(prompt("Inserire giorno: => "));

let monthDaies;
switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
            monthDaies = 31;
    break;
    case 2:
        if ((year % 4) == 0 || (year % 400) == 0) {
            monthDaies = 29;
        } else {
            monthDaies = 28;
        }
    break;
    default:
        monthDaies = 30;
}

const monthInYear = 12;

if (day >= monthDaies) {
    day = 1;
    month = month + 1;
} 
else { 
    day = day + 1; 
}

if (month > monthInYear) {
    month = 1;
    year = year + 1;
}    

console.log(year + "-" + month.toString().padStart(2,"0") + "-" + day.toString().padStart(2,"0"));