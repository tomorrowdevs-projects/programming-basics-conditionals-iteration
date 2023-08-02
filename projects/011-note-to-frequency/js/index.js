/* 
The following table lists an octave of music notes, beginning with middle C, along with their frequencies.

Note	Frequency (Hz)
C4	261.63
D4	293.66
E4	329.63
F4	349.23
G4	392.00
A4	440.00
B4	493.88
Begin by writing a program that reads the name of a note from the user and displays the note’s frequency.
Your program should support all the notes listed previously.

Once you have your program working correctly for the notes listed previously you should add support for all the notes from C0 to C8.
While this could be done by adding many additional cases to your if statement, such a solution is cumbersome, inelegant and unacceptable for the purposes of this exercise. Instead, you should exploit the relationship between notes in adjacent octaves. In particular, the frequency of any note in octave n is half the frequency of the corresponding note in octave n + 1. By using this relationship, you should be able to add support for the additional notes without adding additional cases to your if statement.

Hint:
You will want to access the characters in the note entered by the user individually when completing this exercise.
Begin by separating the letter from the octave.
Then compute the frequency for that letter in the fourth octave using the data in the table above. Once you have this frequency you should divide it by 24−x , where x is the octave number entered by the user. This will halve or double the frequency the correct number of times.

Example:
Input = F6
Output = 1396.9

Input = B0
Output = 30.8
*/

const prompt = require('prompt-sync')({sigint: true}); // Added node module

// Defining the core variables
const C4 =	261.63;
const D4 =	293.66;
const E4 =	329.63;
const F4 =	349.23;
const G4 =	392.00;
const A4 =	440.00;
const B4 =	493.88;


// Using a do...while loop to be sure that the user insert the right input
let note;
do {
    note = prompt("Indica il nome di una nota, in notazione internazioneale (es: Do4 = C4): => ");
} while (isNaN(note[0]) != true || note.length != 2 || isNaN(note[1]) != false); // Used the isNaN method to discrimate inside the input between numbers and strings data types

// Storing the values of the two digit length input, separately
const octave = note[1];
note = note[0].toUpperCase(); // This statement help me to cover both situation, if the user type lowercase or uppercase as first letter
const frequencyConversitionFactor = Math.pow(2, (4 -  octave));

// Chain of if conditional operators, to show the correct output to the user and to check if the typed octave does not exist
if (note == "C" && octave < 9) {
    console.log((C4 / frequencyConversitionFactor).toFixed(2));

} else if (note == "D" && octave < 9) {
    console.log((D4 / frequencyConversitionFactor).toFixed(2));

} else if (note == "E" && octave < 9) {
    console.log((E4 / frequencyConversitionFactor).toFixed(2));

} else if (note == "F" && octave < 9) {
    console.log((F4 / frequencyConversitionFactor).toFixed(2));

} else if (note == "G" && octave < 9) {
    console.log((G4 / frequencyConversitionFactor).toFixed(2));

} else if (note == "A" && octave < 9) {
    console.log((A4 / frequencyConversitionFactor).toFixed(2));

} else if (note == "B" && octave < 9) {
    console.log((B4 / frequencyConversitionFactor).toFixed(2));

} else {
    console.log("ERRORE DI DIGITAZIONE!, RIAVVIARE IL PROGRAMMA"); // For alls the don't cover casese, i show an error message

}