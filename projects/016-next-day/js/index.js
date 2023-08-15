'use strict';

// Read imput from the user
const getYear = parseFloat(prompt('Enter a 4-digit year'));
const getMonth = parseFloat(prompt('Enter a month between 1 and 12'));
const getDay = parseFloat(prompt('Enter a day between 1 and 31'));

const leapYear =
    (getYear % 400 === 0 && getYear % 100 !== 0) || getYear % 4 === 0;

if (getYear % 400 === 0) {
    `
    ${getYear === leapYear}`;
} else if (getYear % 100 === 0) {
    `${getYear !== leapYear}`;
} else if (getYear % 4 === 0) {
    `${getYear === leapYear}`;
} else {
    `${getYear !== leapYear}`;
}

// if (
//     getDay == 30 &&
//     (getMonth == 4 || getMonth == 6 || getMonth == 9 || getMonth == 11)
// ) {
//     alert(`${getYear}-${getMonth + 1}-01`);
// } else if (
//     getDay < 30 &&
//     (getMonth == 4 || getMonth == 6 || getMonth == 9 || getMonth == 11)
// ) {
//     alert(`${getYear}-${getMonth}-${getDay + 1}`);
// }

const userDay =
    getDay == 30 &&
    (getMonth == 4 || getMonth == 6 || getMonth == 9 || getMonth == 11)
        ? alert(`${getYear}-${getMonth + 1}-01`)
        : getDay < 30 &&
          (getMonth == 4 || getMonth == 6 || getMonth == 9 || getMonth == 11)
        ? alert(`${getYear}-${getMonth}-${getDay + 1}`)
        : getDay > 30 &&
          (getMonth == 4 || getMonth == 6 || getMonth == 9 || getMonth == 11)
        ? alert(
              'The month entered cannot have 31 days. You are asked to retype the year, month and day.'
          )
        : getDay == 31 &&
          (getMonth == 1 ||
              getMonth == 3 ||
              getMonth == 5 ||
              getMonth == 7 ||
              getMonth == 8 ||
              getMonth == 10)
        ? alert(`${getYear}-${getMonth + 1}-01`)
        : getDay < 31 &&
          (getMonth == 1 ||
              getMonth == 3 ||
              getMonth == 5 ||
              getMonth == 7 ||
              getMonth == 8 ||
              getMonth == 10 ||
              getMonth == 12)
        ? alert(`${getYear}-${getMonth}-${getDay + 1}`)
        : getDay > 31 &&
          (getMonth == 1 ||
              getMonth == 3 ||
              getMonth == 5 ||
              getMonth == 7 ||
              getMonth == 8 ||
              getMonth == 10 ||
              getMonth == 12)
        ? alert(
              'The month entered cannot have 31 days. You are asked to retype the year, month and day.'
          )
        : getDay <= 28 && getMonth == 2 && leapYear
        ? alert(`${getYear}-${getMonth}-${getDay + 1}`)
        : getMonth === 2 &&
          getDay === 28 &&
          getYear % 4 === 0 &&
          getYear % 100 !== 0
        ? alert(`${getYear}-${getMonth + 1}-01`)
        : getDay === 29 && getMonth === 2 && leapYear
        ? alert(`${getYear}-${getMonth + 1}-01`)
        : alert(
              'When you enter as month 2 you cannot enter 29, because the year entered is not leap year.'
          );
