'use strict';

// 1) Create a random number generator
let rouletteNumber = Math.trunc(Math.random() * 37);

// 2) Display the result
if (
    rouletteNumber == 1 ||
    rouletteNumber == 3 ||
    rouletteNumber == 5 ||
    rouletteNumber == 14 ||
    rouletteNumber == 16 ||
    rouletteNumber == 18 ||
    rouletteNumber == 19 ||
    rouletteNumber == 21 ||
    rouletteNumber == 23 ||
    rouletteNumber == 25 ||
    rouletteNumber == 27 ||
    rouletteNumber == 30 ||
    rouletteNumber == 32 ||
    rouletteNumber == 34 ||
    rouletteNumber == 36
) {
    alert(
        `The spin resulted is ${rouletteNumber}. Pay ${rouletteNumber}. Pay red`
    );
} else if (rouletteNumber === 0) {
    alert(
        `The spin resulted is ${rouletteNumber}. Pay ${rouletteNumber}. Pay 0`
    );
} else if (rouletteNumber === '00') {
    alert(
        `The spin resulted is ${rouletteNumber}. Pay ${rouletteNumber}. Pay 00`
    );
} else {
    alert(
        `The spin resulted is ${rouletteNumber}. Pay ${rouletteNumber}. Pay black`
    );
}

// 3) Display if the number is odd or even

const getNumber =
    rouletteNumber % 2 === 1 ? alert(`Pay Odd`) : alert(`Pay Even`);

// 4) Display if the number is between 1 and 18 or 19 and 36

const halfNumber =
    rouletteNumber >= 1 && rouletteNumber <= 18
        ? alert(`Pay 1 to 18`)
        : alert(`Pay 19 to 36`);
