const prompt = require('prompt-sync')({sigint: true});

let word = prompt("Inserisci una parola: => ");

const wordLength = word.length;
let counter = 0;

for ( let i = 0, z = (wordLength - 1); i < wordLength ; i++, z--) {
    counter = (word[i] === word[z]) ? (counter + 1) : 0;
}

(counter === wordLength) ? console.log(word + " è palindromo!") : console.log(word + " non è palindromo!");