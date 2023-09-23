'use strict';

// For loop with increment + 5
for (let originalPrice = 4.95; originalPrice < 29.95; originalPrice += 5) {
    console.log(originalPrice);

    // store the discount and the new price in a variable
    // Method to.Fixed(2) to have only 2 decimal numbers
    const discountAmount = ((originalPrice / 100) * 60).toFixed(2);
    const newPricePurchase = (originalPrice - discountAmount).toFixed(2);
    alert(
        `The original price is $${originalPrice}; the discount amount is $${discountAmount} and the new price for purchase is $${newPricePurchase}`
    );
}
