/*
A particular cell phone plan includes for € 15.00 a month: 
- 50 minutes of air time 
- 50 text messages    
- Each additional minute of air time costs € 0.25
- Each additional text messages cost € 0.15  
- All cell phone bills include an additional charge of € 0.44 to support 911 call centers

The entire bill (including the 911 charge) is subject to **5 percent sales tax**.  

Write a program that **reads the number of minutes and text messages used in a month** from the user.  
Display:
- Base charge,
- Extra minutes charge (if any),
- Extra text message charge (if any),
- 911 fee, 
- Tax,
- Total bill amount.   

Only display the additional minute and text message charges if the user incurred costs in these categories. 
Ensure that all the charges are displayed **using 2 decimal places**.

Example:   
Input minutes: 500  
Input messages: 55  

Output:  
Base charge: 15.00€  
Extra minutes charge: 112.50€  
Extra messages charge: 0.75€  
911 fee: 0.44€  
Tax: 6.43€  
Total bill amount: 135.12€
*/
const prompt = require('prompt-sync')({sigint: true});

const phonePlanPrice = 15.00;
const charge911 = 0.44;
const salesTax = 0.05;

let minutes;
let messages;
do {
    minutes = prompt("Minuti utilizzati questo mese: => ");
    messages = prompt("Messaggi inviati questo mese: => ");
} while (Number.isInteger(Number(minutes)) != true || Number.isInteger(Number(messages)) != true );

let extraMinutesPrice;
let extraMessagesPrice;
let extraMinutesBill;
let extraMessageBill;

if (minutes > 50) {
    extraMinutesPrice = (minutes - 50) * 0.25;
    extraMinutesBill = "\nCosto Minuti Extra: " + extraMinutesPrice.toFixed(2) + " €";
} 
else {extraMinutesPrice = 0;}

if (messages > 50) {
    extraMessagesPrice = (messages - 50) * 0.15;
    extraMessageBill = "\nCosto Messaggi Extra: " + extraMessagesPrice.toFixed(2) + " €";
} 
else {extraMessagesPrice = 0;}


const extra = extraMessagesPrice + extraMinutesPrice;
const tax = salesTax * (phonePlanPrice + charge911 + extra);
const totalBillPrice = phonePlanPrice + charge911 + tax + extra;

if (extraMinutesPrice != 0 && extraMessagesPrice != 0) {
    console.log("\nDETTAGLI BOLLETTA:\nTariffa Base: " + phonePlanPrice + " €" + extraMinutesBill + extraMessageBill + "\nCosto fisso 911: " + charge911 + " €" + "\nTasse: " + tax.toFixed(2) + " €" + "\nCosto Totale Bolletta: " + totalBillPrice.toFixed(2) + " €");
} 
else if (extraMinutesPrice != 0) {
    console.log("\nDETTAGLI BOLLETTA:\nTariffa Base: " + phonePlanPrice + " €" + extraMinutesBill + "\nCosto fisso 911: " + charge911 + " €" + "\nTasse: " + tax.toFixed(2) + " €" + "\nCosto Totale Bolletta: " + totalBillPrice.toFixed(2) + " €");
} 
else if (extraMessagesPrice != 0) {
    console.log("\nDETTAGLI BOLLETTA:\nTariffa Base: " + phonePlanPrice + " €" + extraMessageBill + "\nCosto fisso 911: " + charge911 + " €" + "\nTasse: " + tax.toFixed(2) + " €" + "\nCosto Totale Bolletta: " + totalBillPrice.toFixed(2) + " €");
}
else {
    console.log("\nDETTAGLI BOLLETTA:\nTariffa Base: " + phonePlanPrice + " €" + "\nCosto fisso 911: " + charge911 + " €" + "\nTasse: " + tax.toFixed(2) + " €" + "\nCosto Totale Bolletta: " + totalBillPrice.toFixed(2) + " €");
}