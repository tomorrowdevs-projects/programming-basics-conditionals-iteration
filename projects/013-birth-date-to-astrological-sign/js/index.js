/*
The horoscopes commonly reported in newspapers use the position of the sun at 
the time of one’s birth to try and predict the future.    
This system of astrology divides the year into twelve zodiac signs, as outline in the table below:  


| Zodiac Sign |       Date Range           |
|-------------|----------------------------|
| Capricorn   | December 22 to January 19  |
| Aquarius    | January 20 to February 18  |
| Pisces      | February 19 to March 20    |
| Aries       | March 21 to April 19       |
| Taurus      | April 20 to May 20         |
| Gemini      | May 21 to June 20          |
| Cancer      | June 21 to July 22         |
| Leo         | July 23 to August 22       |
| Virgo       | August 23 to September 22  |
| Libra       | September 23 to October 22 |
| Scorpio     | October 23 to November 21  |
| Sagittarius | November 22 to December 21 |

Write a program that asks the user to **enter his or her month and day of birth**.    
Then your program should **return the user’s zodiac sign** as part of an appropriate output message.

Example:   
Month input: December   
Day input: 22   
Output: Capricorn  
*/

const prompt = require('prompt-sync')({sigint: true});

let dateBirth = prompt("Inserisci il mese e il giorno della tua nascita: => ");
dateBirth = dateBirth.split(" ");
const month = dateBirth[0].toUpperCase();
const day = dateBirth[1];

if (day > 0 && day <= 31) {

    if (month == "GENNAIO") { (day >= 20) ? console.log("Aquarius"): console.log("Capricorn")}
    else if (month == "FEBBRAIO") { (day >= 19) ? console.log("Pisces"): console.log("Aquarius")}
    else if (month == "MARZO") { (day >= 21) ? console.log("Aries"): console.log("Pisces")}
    else if (month == "APRILE") { (day >= 20) ? console.log("Taurus"): console.log("Aries")}
    else if (month == "MAGGIO") { (day >= 21) ? console.log("Gemini"): console.log("Taurus")}
    else if (month == "GIUGNO") { (day >= 21) ? console.log("Cancer"): console.log("Gemini")}
    else if (month == "LUGLIO") { (day >= 23) ? console.log("Leo"): console.log("Cancer")}
    else if (month == "AGOSTO") { (day >= 23) ? console.log("Virgo"): console.log("Leo")}
    else if (month == "SETTEMBRE") { (day >= 23) ? console.log("Libra"): console.log("Virgo")}
    else if (month == "OTTOBRE") { (day >= 23) ? console.log("Scorpio"): console.log("Libra")}
    else if (month == "NOVEMBRE") { (day >= 22) ? console.log("Sagittarius"): console.log("Scorpio")}
    else if (month == "DICEMBRE") { (day >= 22) ? console.log("Capricorn"): console.log("Sagittarius")}
    
    else { console.log("ERRORE! INSERIRE DATI CORRETTI."); }

} else {
    console.log("ERRORE! INSERIRE DATI CORRETTI.");
}