'use strict';

let num = Math.floor(Math.random() * 100) + 1;
let updates = 0;
console.log(`${num} is the first Maximum Integer`);

for (let i = 0; i < 99; i++) {
    let i = Math.floor(Math.random() * 100) + 1;
    console.log(`${i} Update`);
    if (i > num) {
        num = i;
        updates++;
        console.log(`${i} <== Update`);
    }
}
console.log(`Maximum value encountered: ${num}`);
console.log(`Number of updates performed: ${updates}`);
