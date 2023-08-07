'use strict';

// I inserted the .toLowerCase() method to convert what the user entered into italics. As the user can also enter a letter in uppercase
const userLetter = prompt(
    'Please enter a letter of the alphabet'
).toLowerCase();

// I used a ternary operator to create the various options and the OR operator
const typeUserLetter =
    userLetter === 'a' ||
    userLetter === 'e' ||
    userLetter === 'i' ||
    userLetter === 'o' ||
    userLetter === 'u'
        ? alert(`The entered letter is a vowel.`)
        : userLetter === 'y'
        ? alert(
              `Sometimes ${userLetter} is a vowel, and sometimes ${userLetter} is a consonant.`
          )
        : userLetter === 'b' ||
          userLetter === 'c' ||
          userLetter === 'd' ||
          userLetter === 'f' ||
          userLetter === 'g' ||
          userLetter === 'h' ||
          userLetter === 'j' ||
          userLetter === 'k' ||
          userLetter === 'l' ||
          userLetter === 'm' ||
          userLetter === 'n' ||
          userLetter === 'p' ||
          userLetter === 'q' ||
          userLetter === 'r' ||
          userLetter === 's' ||
          userLetter === 't' ||
          userLetter === 'v' ||
          userLetter === 'w' ||
          userLetter === 'x' ||
          userLetter === 'z'
        ? alert(`The entered letter is a consonant`)
        : alert(`Incorrect data entry. Please enter a letter of the alphabet`);
