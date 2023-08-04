/*
In this exercise you will create a program that:
- **computes the average of a collection of values entered by the user**.   
- The user will enter **0 as a sentinel value** to indicate that no further values will be provided. 
- **display an appropriate error message if the first value entered by the user is 0**.  

**Hint**: Because the 0 marks the end of the input it should not be included in the average.
*/

const prompt = require('prompt-sync')({sigint: true});

let input = Number(prompt("Inserisci un numero: => "));

if (input == 0) {

    console.log("ERRORE! Inserire uno 0 solo al termine dei valori di cui fare la media!");
   
}
else {

    let sum = 0;
    for (i = 0; input != 0; i++) {   
        sum = sum + input;
        input = Number(prompt("Inserisci un numero: => "));
    }

    const average = sum / i;
    console.log(average);

}

