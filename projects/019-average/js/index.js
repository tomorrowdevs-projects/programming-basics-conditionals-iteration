'use strict';

let sum = 0;
let count = 0;
let value;

do {
    value = parseFloat(
        prompt(
            `Enter one number at a time and enter 0 if you want to interrupt the number sequence.`
        )
    );

    if (value === 0) {
        if (count === 0) {
            alert(`Error: The first value could not be 0`);
        } else {
            break;
        }
    }

    sum += value;
    count++;
} while (true);

if (count === 0) {
    `No value was entered`;
} else {
    const average = sum / count;
    alert(`Average of entered values: ${average.toFixed(2)}`);
}
