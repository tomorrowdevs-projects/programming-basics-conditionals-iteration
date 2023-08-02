/* 
The length of a month varies from 28 to 31 days.   
In this exercise you will create a program that reads **the name of a month** from the user as a string.   
Then your program should display the number of days in that month.   
Display **28 or 29 days** for **February** so that leap years are addressed.  

Example:  
Input = April  
Output = 30
*/

const prompt = require('prompt-sync')({sigint: true});

const month = prompt("Inserisci il nome di un mese: => ");

switch (month) {

    case "Gennaio":
    case "Marzo":
    case "Maggio":
    case "Luglio":
    case "Agosto":
    case "Ottobre":
    case "Dicembre":
        console.log("Questo mese è di 31 giorni");
    break;

    case "Aprile":
    case "Giugno":
    case "Settembre":
    case "Novembre":
        console.log("Questo mese è di 30 giorni");
    break;

    case "Febbraio":
        console.log("Questo mese è di 28 o 29 giorni");
    break;

    default:
        console.log("ERRORE! Inserie un input valido!\nPer favore riavviare il programma!");

}