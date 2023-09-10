let count = 0; // Questa variabile per contare uguali
let previousNumber = null; // Questa variabile per memorizzare il numero precedente;
let flips = 1; // Questa variabile per memorizzare i tentativi in totale quando l'iterazione si interrompe;
for (let i = 0; i < 10; i++) { //reitero il loop annidato per 10 volte
    for (let i = 0; i < 50; i++) {
        let randomNumber = Math.floor(Math.random() * 2) + 1; // Genera un numero casuale tra 1 e 2;

        if (randomNumber === previousNumber) {
            count++; // Incremento il conteggio se il numero attuale è uguale a quello precedente
        } else {
            count = 1; // Reimposto il count se il numero è diverso;
        }

        if (randomNumber === 1) {
            console.log('H');
        } else {
            console.log('T');
        }

        if (count === 3) {
            break;
        }

        previousNumber = randomNumber; // Salvo il mumero attuale come numero precedente per la prossima reiterazione;
        flips++;
    }
    console.log(`${flips} flips`);
}
console.log(`On average, ${flips / 10} flips were needed.`);
