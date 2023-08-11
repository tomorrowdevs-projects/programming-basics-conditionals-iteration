'use strict';

// Wrrite variables
const frequencyNoteC4 = 261.63;
const frequencyNoteD4 = 293.66;
const frequencyNoteE4 = 329.63;
const frequencyNoteF4 = 349.23;
const frequencyNoteG4 = 392.0;
const frequencyNoteA4 = 440.0;
const frequencyNoteB4 = 493.88;

// Read input from the user
const getLetter = prompt(`Enter a letter between a and h`).toUpperCase();
const getOctave = parseFloat(prompt(`Insert a number between 0 and 8`));
// Stored in a variable the divider
const divideNumber = 2 ** (4 - getOctave);

if (getLetter === 'a'.toUpperCase()) {
    alert(
        `Input = ${getLetter}${getOctave}; Output = ${
            frequencyNoteA4 / divideNumber
        }`
    );
} else if (getLetter === 'b'.toUpperCase()) {
    alert(
        `Input = ${getLetter}${getOctave}; Output = ${
            frequencyNoteB4 / divideNumber
        }`
    );
} else if (getLetter === 'c'.toUpperCase()) {
    alert(
        `Input = ${getLetter}${getOctave}; Output = ${
            frequencyNoteC4 / divideNumber
        }`
    );
} else if (getLetter === 'd'.toUpperCase()) {
    alert(
        `Input = ${getLetter}${getOctave}; Output = ${
            frequencyNoteD4 / divideNumber
        }`
    );
} else if (getLetter === 'e'.toUpperCase()) {
    alert(
        `Input = ${getLetter}${getOctave}; Output = ${
            frequencyNoteE4 / divideNumber
        }`
    );
} else if (getLetter === 'f'.toUpperCase()) {
    alert(
        `Input = ${getLetter}${getOctave}; Output = ${
            frequencyNoteF4 / divideNumber
        }`
    );
} else if (getLetter === 'g'.toUpperCase()) {
    alert(
        `Input = ${getLetter}${getOctave}; Output = ${
            frequencyNoteG4 / divideNumber
        }`
    );
} else {
    alert(`Enter a correct letter and a correct number`);
}
