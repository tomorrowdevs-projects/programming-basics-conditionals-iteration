'use strict';

let q = parseFloat(prompt('Enter a decimal number')); // Dichiaro una variabile
let result = '';

while (q > 0) {
    if (q % 2 === 0) {
        result = '0' + result; // memorizzo il risultato in result
    } else {
        result = '1' + result;
    }
    q = Math.floor(q / 2);
}
alert(
    `The binary representation of the decimal number ${q} is as follows: '${result}'`
);
