'use strict';

let number = parseFloat(prompt('Enter an integer (2 or greater)'));
let fattore = 2;

while (number < 2) {
    console.log('Insert a number greater or equal than 2');
    break;
}
while (number > 1) {
    if (number % fattore === 0) {
        console.log(fattore);
        number = number / fattore;
    } else {
        fattore++;
    }
    console.log(`For the ${number} ci sono i seguenti numeri: ${fattore};`);
}
