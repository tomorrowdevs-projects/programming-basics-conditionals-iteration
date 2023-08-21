const prompt = require('prompt-sync')({sigint: true});

let q = Number(prompt("Inserisci un numero intero: => "));

let result = "";
while (q != 0) {
    const r =  (q % 2).toString();
    result = r + result;
    q = Math.trunc(q / 2);
}

console.log("Conversione in binario: => " + result);