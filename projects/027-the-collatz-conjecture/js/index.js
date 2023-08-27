'use strict';

let num = 0;
while (true) {
    let numCollatz = parseFloat(prompt('Enter a positive digit number'));

    if (numCollatz <= 0 || numCollatz === 1) {
        break;
    }

    if (numCollatz % 2 === 1) {
        alert(numCollatz * 3 + 1);
    } else if (numCollatz % 2 === 0) {
        alert(numCollatz / 2);
    } else {
        console.log('Insert a number');
    }
}
