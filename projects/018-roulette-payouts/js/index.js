/*
A roulette wheel has **38 spaces** on it.   
Of these spaces:
- 18 are red, numbered 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36.
- 18 are black, the remaining integers between 1 and 36 are used to number the black spaces.
- 2 are green, numbered 0 and 00   

Many different bets can be placed in roulette. 
We will only consider the following subset of them in this exercise:
- Single number (1 to 36, 0, or 00)
- Red versus Black
- Odd versus Even (Note that 0 and 00 do not pay out for even) 
- 1 to 18 versus 19 to 36

Write a program that simulates a spin of a roulette wheel **by using a random number generator**.   
Display **the number that was selected and all the bets that must be paid**. 

For example, if 13 is selected then your program should display:

```
The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18
```

If the simulation results in 0 or 00 then your program should display `Pay 0` or `Pay 00` without any further output.
*/

let spinResultNumber = Math.round((Math.random() * 37));

if (spinResultNumber >= 36.5) {
    spinResultNumber = "00";
}

console.log("Il numero estratto è: " + spinResultNumber);
console.log("Paga: " + spinResultNumber);

const red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36];
const green = [0,"00"];



if (spinResultNumber != 0 && spinResultNumber != "00") {

    (red.includes(spinResultNumber)) ? console.log("Paga: Rosso") : console.log("Paga: Nero");

    ((spinResultNumber % 2) == 0) ? console.log("Paga: Pari") : console.log("Paga: Dispari");

    ((spinResultNumber / 2) >= 9.5) ? console.log("Paga: 19 - 36") : console.log("Paga: 1 - 18");

} 
else {

    console.log("Paga: Verde");

}

