const prompt = require('prompt-sync')({sigint: true});

let daiesOfVacation;
let moneyBudget;

while (true) {
    daiesOfVacation = Number( prompt("Per quanti giorni sarai in vacanza? => ") );
    moneyBudget = Number( prompt("Qual'è il tuo budget monetario? => ") );

    if ( isNaN( (daiesOfVacation + moneyBudget) ) || daiesOfVacation <= 0 || Number.isInteger(daiesOfVacation) == false || moneyBudget <= 0 ) {
        console.log("Inserisci valori coerenti con la richiesta!");
    }
    else {
        break;
    }
}


let totalPurchases;

while (true) {

    let totalAccomodation = 0;
    let totalTransport = 0;
    let totalMeals = 0;
    let totalShoppingPurchases = 0;
        
    for (let i = 1; i <= daiesOfVacation; i++) {

        const accomodation = Number( prompt("Quanto hai speso giorno " + i + ", per l'alloggio? => ") );
        const transport = Number( prompt("Quanto hai speso giorno " + i + ", per i trasporti? => ") );
        const meals = Number( prompt("Quanto hai speso giorno " + i + ", per i pasti? => ") );
        const shoppingPurchases = Number( prompt("Quanto hai speso giorno " + i + ", per lo shopping(regali, tickets, vestiti, ecc..)? => ") );

        if ( isNaN( (accomodation + transport + meals + shoppingPurchases) ) || accomodation < 0 || transport < 0 || meals < 0 || shoppingPurchases < 0) {
            console.log("ERRORE! Controlla attentamente gli importi e inseriscili nuovamente!");
            i--;
            continue;
        }

        totalAccomodation += accomodation;
        totalTransport += transport;
        totalMeals += meals;
        totalShoppingPurchases += shoppingPurchases;
    }

    totalPurchases = totalAccomodation + totalTransport + totalMeals + totalShoppingPurchases;

    console.log("\nDurante i " + daiesOfVacation + " giorni di vacanza, hai speso: \n- " + totalAccomodation + " euro per gli allogi\n- " + totalTransport + " euro per i trasporti\n- " + totalMeals + " euro per i pasti\n- " + totalShoppingPurchases + " euro per gli acquisti vari\n" + "Totale spesa: " + totalPurchases + " euro.\n");

    let userPurchasesCheck;

    do {
        userPurchasesCheck = prompt("Per favore controlla gli importi di spesa. Sono corretti(si/no)? => ").toLowerCase();
    } while (userPurchasesCheck !== "no" && userPurchasesCheck !== "si");

    if (userPurchasesCheck === "no") {
        console.log("Ti prego di inserire nuovamente gli importi di spesa sostenuti.");
    } 
    else if (userPurchasesCheck === "si") {
        break;
    }
}

const moneyLeft = moneyBudget - totalPurchases;

if (moneyLeft < 0) {
    console.log("Oh no! Hai speso " + (moneyLeft * -1) + " euro più del previsto!");
} 
else {
    console.log("Complimenti! Sei rimasto nel budget!" + "\nSaldo: " + moneyLeft + " euro.");
}