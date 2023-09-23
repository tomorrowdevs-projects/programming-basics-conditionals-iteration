'use strict';
// Read imput from the user
const getYear = parseFloat(prompt('Enter a year'));
const dayOfWeek =
    (getYear +
        Math.floor((getYear - 1) / 4) -
        Math.floor((getYear - 1) / 100) +
        Math.floor((getYear - 1) / 400)) %
    7;

const getDayOfTheWeek =
    dayOfWeek === 0
        ? alert(`Input: ${getYear}; Output: Sunday`)
        : dayOfWeek === 1
        ? alert(`Input: ${getYear}; Output: Monday`)
        : dayOfWeek === 2
        ? alert(`Input: ${getYear}; Output: Tuesday`)
        : dayOfWeek === 3
        ? alert(`Input: ${getYear}; Output: Wednesday`)
        : dayOfWeek === 4
        ? alert(`Input: ${getYear}; Output: Thursday`)
        : dayOfWeek === 5
        ? alert(`Input: ${getYear}; Output: Friday`)
        : dayOfWeek === 6
        ? alert(`Input: ${getYear}; Output: Saturday`)
        : alert('You have not entered a number');
