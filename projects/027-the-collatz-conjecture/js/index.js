const prompt = require('prompt-sync')({sigint: true});

while (true) {
    let number = Number(prompt("Inserisci un numero intero positivo o premi un altro tasto per uscire: => "));

    if (number <= 0 || isNaN(number) || Number.isInteger(number) != true) {
      break;
    }
    const firstNumber = number;
    let sequence = "";
    
    do {
        switch(number % 2 === 0) {
        case true:
        number = number / 2;
        break;
        case false:
        number = number * 3 + 1;
        break;
    }
        sequence = sequence + ","  + number;

    } while (number != 1)

    console.log("Sequenza di numeri: => " + firstNumber + sequence);
}