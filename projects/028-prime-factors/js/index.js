'use strict';

let userInput = Number(prompt('Enter an integer (2 or greater)'));
let factor = 2;

while (userInput < 2 || isNaN(userInput)) {
    console.log('Insert an integer greater or equal than 2');
    userInput = Number(prompt('Enter an integer (2 or greater)'));
}
while (userInput > 1) {
    if (userInput % factor === 0) {
        console.log(factor);
        userInput = userInput / factor;
    } else {
        factor++;
    }
}
