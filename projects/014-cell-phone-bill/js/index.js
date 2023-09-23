'use strict';
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
