'use strict';
/* A particular cell phone plan includes for € 15.00 a month:

50 minutes of air time
50 text messages
Each additional minute of air time costs € 0.25
Each additional text messages cost € 0.15
All cell phone bills include an additional charge of € 0.44 to support 911 call centers
The entire bill (including the 911 charge) is subject to 5 percent sales tax.

1) Write a program that reads the number of minutes and text messages used in a month from the user.

2) Only display the additional minute and text message charges if the user incurred costs in these categories. 

3) Ensure that all the charges are displayed using 2 decimal places.

*/
const baseCharge = 15.0;
const minutesAirTime = 50;
const textMessages = 50;
const priceAdditionalMinute = 0.25;
const priceAdditionalMessage = 0.15;
const callCenterFee = 0.44;

// Read imput from the user
const inputMinutes = parseFloat(
    prompt('Enter the number of minutes used in this month')
);
const inputMessages = parseFloat(
    prompt('Enter the number of messages used in this month')
);

// Calculating cost of extra minutes and messages
const extraMinutes =
    inputMinutes >= 51
        ? priceAdditionalMinute * (inputMinutes - minutesAirTime)
        : 0.0;

const extraMessages =
    inputMessages >= 51
        ? priceAdditionalMessage * (inputMessages - textMessages)
        : 0;

// // The number method to have a number in return and not a string
const percentSalesTax = Number(
    (
        ((baseCharge + extraMinutes + extraMessages + callCenterFee) / 100) *
        5
    ).toFixed(2)
);

const totalBillAmount = Number(
    baseCharge + extraMinutes + extraMessages + callCenterFee + percentSalesTax
);

const cellPhoneBill =
    alert(`Input minutes: ${inputMinutes}; Input messages: ${inputMessages}
Output:
Base charge: ${baseCharge.toFixed(2)}€;
Extra minutes charge: ${extraMinutes.toFixed(2)}€;
Extra messages charge: ${extraMessages.toFixed(2)}€;
911 fee: ${callCenterFee}€;
Tax: ${Number(percentSalesTax.toFixed(2))}€;
Total bill amount: ${totalBillAmount.toFixed(2)}€`);
