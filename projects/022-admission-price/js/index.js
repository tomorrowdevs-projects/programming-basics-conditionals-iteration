/*
A particular zoo determines the price of admission based on the age of the guest.   
- Guests 2 years of age and less are admitted without charge. 
- Children between 3 and 12 years of age cost $14.00.
- Seniors aged 65 years and over cost $18.00. 
- Admission for all other guests is $23.00.  

Create a program that begins by **reading the ages of all the guests in a group from the user**, 
with one age entered on each line.   
The user will enter a **blank lin**e (a newline character) to indicate that there are no more guests in the group.    
Then your program should display the admission cost for the group with an appropriate message.   
The cost should be displayed using **two decimal places**.
*/

const prompt = require('prompt-sync')({sigint: true});

// const groupMembers = parseInt(prompt("Quanti siete nel gruppo? => "));

let priceTotal = 0;
while (true) /* (let i = 0; i < groupMembers; i++) */{
    
const age = prompt("Inserire età degli ospiti: => ");
    if (age === "") {
        break;
    }

const priceTicket = (age < 3) ? 0 : (age >= 3 && age <= 12) ? 14 : (age >= 65) ? 18 : 23;

priceTotal = priceTicket + priceTotal;
}

console.log ("Prezzo totale dei biglietti: " + priceTotal.toFixed(2) + " $");