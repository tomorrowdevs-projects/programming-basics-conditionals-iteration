'use strict';

// Read imput from the user
const inputYear = parseFloat(prompt('Enter a year'));

// Exercise resolution
if (inputYear % 400 === 0) {
    alert(`The ${inputYear} is a leap year`);
} else if (inputYear % 100 === 0) {
    alert(`The ${inputYear} is not a leap year`);
} else if (inputYear % 4 === 0) {
    alert(`The ${inputYear} is a leap year`);
} else {
    alert(`The ${inputYear} is not a leap year`);
}
