'use strict';

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
