const prompt = require('prompt-sync')({sigint: true});

let message = prompt("Inserisci il testo da cifrare: => ");
const encodingKey = parseInt(prompt("Inserisci la chiave di codifica/decodifica (come un numero intero): => "));

message = message.split("");
let encryptedMessage = "";

for (let i = 0; i < message.length; i++) {

    let decimalValue = message[i].charCodeAt();
    let newDecimalValue = decimalValue + encodingKey;

    if (decimalValue >= 65 && decimalValue <= 90) {
        
        newDecimalValue = (newDecimalValue > 90) ? 
        (64 + (encodingKey - (90 - decimalValue))) : (newDecimalValue < 65) ? 
        (91 + (encodingKey - (65 - decimalValue))) : newDecimalValue;

        message[i] =  String.fromCharCode(newDecimalValue);

    }
    else if (decimalValue >= 97 && decimalValue <= 122) {

        newDecimalValue = (newDecimalValue > 122) ? 
        (96 + (encodingKey - (122 - decimalValue))) : (newDecimalValue < 97) ? 
        (123 + (encodingKey - (97 - decimalValue))) : newDecimalValue;

        message[i] =  String.fromCharCode(newDecimalValue);

    }

    encryptedMessage = encryptedMessage + message[i];
}

console.log(encryptedMessage);

/* let newMessage = "";
for (let i = 0; i < message.length; i++) {
    const decimalValue = message.charAt(i).charCodeAt()
    if ( (decimalValue >= 65 && decimalValue <= 90) ||  (decimalValue >= 97 && decimalValue <= 122) ) {

        newMessage = newMessage + String.fromCharCode(decimalValue + encodingKey);
    } else {
        newMessage = newMessage + message.charAt(i);
    }
}
console.log(newMessage); */
