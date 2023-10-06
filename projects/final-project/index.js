'use strict';

// Input user
let travelDays = parseFloat(
    prompt('Enter the total number of days of your trip')
);
let totalBudget = parseFloat(
    prompt('Enter the total budget available in euros')
);

let totalExpense = 0; // Initialise the total expense

while (true) {
    let newCategory = prompt(
        'Enter an expense category or type "end" to finish'
    ).toLowerCase();

    if (newCategory === 'end') {
        break; // Loop exits when user enters end;
    }
    let totalCostCategory = 0; // Initialise the total cost for the entered category

    for (let day = 1; day <= travelDays; day++) {
        let dailyCostCategory = parseFloat(
            prompt(`Enter how much you spent on ${newCategory} on day ${day}`)
        );
        console.log(
            `On day ${day}, I spent €${dailyCostCategory.toFixed(
                2
            )} on ${newCategory}.`
        );

        totalCostCategory += dailyCostCategory; // Accumulate daily expenses

        // Stored a variable to ask the user if he needs to change something
        let modifyCost = prompt(
            `Do you need to change the entered expence on this day for the category ${newCategory.toUpperCase()}? Yes or No?`
        ).toLowerCase();

        while (modifyCost === 'yes') {
            //While loop for handling exceptions

            // Initialise a new variable to store the new entered cost
            let newCost = parseFloat(
                prompt(`Enter the new amount for day ${day}`)
            );

            totalCostCategory += newCost - dailyCostCategory; // Accumulate daily expenses with the difference between the new cost and the incorrect cost

            console.log(
                `On day ${day}, I spent €${newCost} on the category ${newCategory}.`
            );

            // Ask the user again if they want to change the amount they have just entered
            modifyCost = prompt(
                'Do you need to change the newly entered amount? Yes or No?'
            ).toLowerCase();
        }
    }
    console.log(
        `For the category ${newCategory} you spent a total €${totalCostCategory.toFixed(
            2
        )}`
    );

    totalExpense += totalCostCategory; // Accumulate total expenses by category
}

totalExpense = alert(
    // Total expense
    `For an ${travelDays}-day holiday you spent in total €${totalExpense.toFixed(
        2
    )}`
);

// Check that the total expense  has not exceeded the initial available budget
if (totalExpense <= totalBudget) {
    alert('You stuck to the initial budget');
} else {
    alert('You exceed your initial budget');
}
