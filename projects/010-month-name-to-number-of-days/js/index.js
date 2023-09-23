'use strict';
/*Month Name to Number of Days
The length of a month varies from 28 to 31 days.

1) In this exercise you will create a program that reads the name of a month from the user as a string.
2)Then your program should display the number of days in that month.
3) Display 28 or 29 days for February so that leap years are addressed.

Example:
Input = April
Output = 30*/

// I used the .toLowerCase() method to convert the prompt to LowerCase
const month = prompt(`Please enter the name of a month`).toLowerCase();

if (
    month === 'april' ||
    month === 'june' ||
    month === 'september' ||
    month === 'november'
) {
    alert(`Input = ${month}
          Output = 30 days`);
} else if (month === 'february') {
    alert(`Input = ${month}
          Output = 28 or 29 days`);
} else if (
    month === 'january' ||
    month === 'march' ||
    month === 'may' ||
    month === 'july' ||
    month === 'august' ||
    month === 'october' ||
    month === 'december'
) {
    alert(`Input = ${month}
          Output = 31 days`);
} else {
    alert(`The data entered is incorrect. Please enter the name of a month.`);
}
