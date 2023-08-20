const prompt = require('prompt-sync')({sigint: true});

let number = Number(prompt("Inserisci un numero intero > 2: => "));

if (number < 2 || isNaN(number) || Number.isInteger(number) != true) {

    console.log("ERRORE!! INSERISCI UN NUMERO VALIDO!")
}
else {
    console.log("\nLa scomposizionie in fattori primi di " + number + " è:")
    for (let factor = 2; number != 1; ) { 

        if (number % factor === 0) {
            number = number / factor;
            console.log(factor);
            continue;
        }

        factor++
    }
}