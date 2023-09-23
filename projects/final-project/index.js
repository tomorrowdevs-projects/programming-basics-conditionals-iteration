'use script';

// User input
let numberTravelDays = parseFloat(
    prompt('Enter the total number of days of your trip')
);
let totalBudget = parseFloat(
    prompt('Enter the total budget available in euros')
);

// Stored the variables for the total
let totalCostsLodging = 0;
let totalCostsTrasport = 0;
let totalCostsMeals = 0;
let totalCostsActivities = 0;
let totalCostsExtras = 0;

let totalExpenditure = 0;

for (;;) {
    // Daily expenses
    for (let day = 1; day <= numberTravelDays; day++) {
        let dayCostsLodging = parseFloat(
            prompt(`Enter how much you spent on accommodation on day ${day}`)
        );
        console.log(
            `On day ${day}, I spent €${dayCostsLodging.toFixed(
                2
            )} on accomodation.`
        );

        let dayCostsTrasport = parseFloat(
            prompt(`Enter how much you spent on transport on day ${day}`)
        );
        console.log(
            `On day ${day}, I spent €${dayCostsTrasport.toFixed(
                2
            )} on trasport.`
        );

        let dayCostsMeals = parseFloat(
            prompt(`Enter how much you spent on food on day ${day}`)
        );
        console.log(
            `On day ${day}, I spent €${dayCostsMeals.toFixed(2)} on trasport.`
        );

        let dayCostsActivities = parseFloat(
            prompt(
                `Enter how much you spent on activities and attractions on day ${day}`
            )
        );
        console.log(
            `On day ${day}, I spent €${dayCostsActivities.toFixed(
                2
            )} on activities and attractions.`
        );

        let dayCostsExtras = parseFloat(
            prompt(`Enter how much you spent on extras on day ${day}`)
        );
        console.log(
            `On day ${day}, I spent €${dayCostsExtras.toFixed(2)} on extras.`
        );
        // Accumulation of daily expenses in total variables by category
        totalCostsLodging += dayCostsLodging;
        totalCostsTrasport += dayCostsTrasport;
        totalCostsMeals += dayCostsMeals;
        totalCostsActivities += dayCostsActivities;
        totalCostsExtras += dayCostsExtras;

        // Stored a variable to ask the user if he needs to change something
        let modifyCosts = prompt(
            'Do you need to change your shopping for this day? Yes or No? '.toLowerCase()
        );

        // While loop for handling exceptions
        while (modifyCosts === 'yes') {
            let modifyCategory = prompt(
                'Enter the category that you need to change between Lodging, Trasport, Meals, Activities or Extras'.toLowerCase()
            );
            // Stored a new variable for the new user input
            let newCosts;

            if (modifyCategory === 'lodging') {
                newCosts = parseFloat(
                    prompt(`Enter the new amount for day ${day}`)
                );
                dayCostsLodging = newCosts;
            } else if (modifyCategory === 'trasport') {
                newCosts = parseFloat(
                    prompt(`Enter the new amount for day ${day}`)
                );
                dayCostsTrasport = newCosts;
            } else if (modifyCategory === 'meals') {
                newCosts = parseFloat(
                    prompt(`Enter the new amount for day ${day}`)
                );
                dayCostsMeals = newCosts;
            } else if (modifyCategory === 'activities') {
                newCosts = parseFloat(
                    prompt(`Enter the new amount for day ${day}`)
                );
                dayCostsActivities = newCosts;
            } else if (modifyCategory === 'extras') {
                newCosts = parseFloat(
                    prompt(`Enter the new amount for day ${day}`)
                );
                dayCostsExtras = newCosts;
            } else {
                alert('You have entered an invalid category.');
            }

            // Accumulation of daily expenses in total variables per category with the difference between the new cost and the incorrect cost
            totalCostsLodging += newCosts - dayCostsLodging;
            totalCostsTrasport += newCosts - dayCostsTrasport;
            totalCostsMeals += newCosts - dayCostsMeals;
            totalCostsActivities += newCosts - dayCostsActivities;
            totalCostsExtras += newCosts - dayCostsExtras;

            console.log(
                `On day ${day}, I spent €${newCosts} on the category ${modifyCategory}.`
            );
            modifyCosts = prompt(
                'Do you need to change your shopping for this day? Yes or No? '.toLowerCase()
            );
        }
    }
    // Calculation of expenses by category
    alert(
        `You spent a total of €${totalCostsLodging.toFixed(
            2
        )} on accomodation for the duration of your ${numberTravelDays}-day holiday.`
    );
    alert(
        `You spent a total of €${totalCostsTrasport.toFixed(
            2
        )} on trasport for the duration of your ${numberTravelDays}-day holiday.`
    );
    alert(
        `You spent a total of €${totalCostsMeals.toFixed(
            2
        )} on meals for the duration of your ${numberTravelDays}-day holiday.`
    );
    alert(
        `You spent a total of €${totalCostsActivities.toFixed(
            2
        )} on activities and attractions for the duration of your ${numberTravelDays}-day holiday.`
    );
    alert(
        `You spent a total of €${totalCostsExtras.toFixed(
            2
        )} on extras for the duration of your ${numberTravelDays}-day holiday.`
    );
    // total expenditure
    totalExpenditure =
        totalCostsLodging +
        totalCostsTrasport +
        totalCostsMeals +
        totalCostsActivities +
        totalCostsExtras;

    alert(
        `For an ${numberTravelDays}-day holiday you spent in total €${totalExpenditure.toFixed(
            2
        )}`
    );
    // condition to check whether or not the user has exceeded the available budget
    if (totalExpenditure <= totalBudget) {
        alert(
            `You have spent a total of €${totalExpenditure} and have not exceeded the initial budget of €${totalBudget}.`
        );
    } else {
        alert(
            `You have spent a total of €${totalExpenditure} and have exceeded the initial budget of €${totalBudget}.`
        );
    }
}
