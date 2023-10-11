'use strict';
let travelDays = Number(prompt('Enter the total number of days of your trip'));
let totalBudget = Number(prompt('Enter the total budget available in euros'));

let totalExpense = 0;

while (true) {
    let newCategory = prompt(
        'Enter an expense category or type "end" to finish'
    ).toLowerCase();

    if (newCategory === 'end') {
        break;
    }
    let totalCostCategory = 0;

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

        let modifyCost = prompt(
            `Do you need to change the entered expence on this day for the category ${newCategory.toUpperCase()}? Yes or No?`
        ).toLowerCase();

        while (modifyCost === 'yes') {
            // Initialise a new variable to store the new entered cost
            let newCost = parseFloat(
                prompt(`Enter the new amount for day ${day}`)
            );

            totalCostCategory += newCost - dailyCostCategory; // Accumulate daily expenses with the difference between the new cost and the incorrect cost

            console.log(
                `On day ${day}, I spent €${newCost} on the category ${newCategory}.`
            );

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

alert(
    `For an ${travelDays}-day holiday you spent in total €${totalExpense.toFixed(
        2
    )}`
);

// Check that the total expense  has not exceeded the initial available budget
if (totalBudget >= totalExpense) {
    alert('You have not exceeded the original budget');
} else {
    alert('You have exceeded your original budget');
}
