'use strict';

let palindromString = prompt('Enter a word');
let isPalindrom = true;

for (let i = 0; i < Math.floor(palindromString.length / 2); i++) {
    // Check if the characters at symmetrical positions are not equal
    if (
        palindromString.charAt(i) !==
        palindromString.charAt(palindromString.length - 1 - i)
    ) {
        isPalindrom = false;
        break;
    }
}

if (isPalindrom) {
    alert(
        `Input: ${palindromString}; Output: ${palindromString} is a palindrome`
    );
} else {
    alert(
        `Input: ${palindromString}; Output: ${palindromString} is not a palindrome`
    );
}
