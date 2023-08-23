
let maximumNumber = 0;
let updateCounter= 0;

for (let i = 0; i < 100; i++) {
    const newNumber = Math.trunc(Math.random()*100) + 1;
    if (newNumber > maximumNumber) {
        console.log(newNumber + " <=== Update!");
        maximumNumber = newNumber;
        updateCounter++;
    }
    else {
        console.log(newNumber);
    }
}

console.log("Valore massimo incontrato: " + maximumNumber);
console.log("Il valore massimo è stato aggiornato " + updateCounter + " volte!");