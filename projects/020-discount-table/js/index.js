/*
Write a program that uses a loop to generate a table for  $4.95, $9.95, $14.95, $19.95 and $24.95 that shows:
- the original price
- the discount amount
- the new price for purchases 

Ensure that the discount amounts and the new prices are **rounded to 2 decimal places** when they are displayed.
*/

const originalPrices = [4.95, 9.95, 14.95, 19.95, 24.95];
const discount = 0.6;

for (let i = 0; i < 5; i++) {
    console.log("\nPrezzo di partenza: => " + originalPrices[i] + " $") ;

    const discountAmount = (originalPrices[i] * discount).toFixed(2);
    console.log("Valore dello sconto del 60%: => " + discountAmount + " $");

    const finalPrice = (originalPrices[i] - discountAmount).toFixed(2);
    console.log("Prezzo finale: => " + finalPrice + " $" + "\n");
}

