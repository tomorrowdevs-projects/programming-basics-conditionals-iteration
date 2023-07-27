/*
Write a program that:
- reads a position from the user.  
- Use an if statement to determine **if the column begins with a black square or a white square**.  
- Then use modular arithmetic to report the color of the square in that row. 
- Your program may assume that a valid position will always be entered. 
- It does not need to perform any error checking.

Example:  
Input =  a1  
Output = black

Input = d5  
Output = white  
*/

// ---------- SOLUTION 1 -----------

/*
    const prompt = require('prompt-sync')({sigint: true});

    let positionPiece = prompt("Inserisci coordinate punto scacchiera: => ");

    if (positionPiece[0] == "a"|| positionPiece[0] == "c"|| positionPiece[0] == "e"|| positionPiece[0] == "g") {
        console.log("The square is: Black!");
        switch (positionPiece[1]) {
            case "1":
            case "3":
            case "5":
            case "7":
                console.log("The square is: Black!");
            break;
            default: console.log("The square is: White!");
        }

    } else if (positionPiece[0] == "b"|| positionPiece[0] == "d"|| positionPiece[0] == "f"|| positionPiece[0] == "h") {

        switch (positionPiece[1]) {
            case "2":
            case "4":
            case "6":
            case "8":
                console.log("The square is: White!");
            break;
            default: console.log("The square is: Black!");
        }

    }
*/


// ----------- SOLUTION 2 (EVOLVED BY ONE) --------------------

const prompt = require('prompt-sync')({sigint: true});

// Checking until the user provide a correct position, unluckly the special characters pass the test
let positionPiece;
do {
    positionPiece = prompt("Inserisci coordinate punto scacchiera: => ");
} while ( isNaN(positionPiece[0]) != true || positionPiece.length != 2 || isNaN(Number(positionPiece[1])) != false || Number(positionPiece[1]) < 1  || Number(positionPiece[1]) > 8 );
    
const column = positionPiece[0].charCodeAt(); // Using the unicode codificatione of the char to manipulate it as a number
const row = positionPiece[1];

// I check for odd and even letters, the same for numbers, and then I return an output in console
if ((column % 2) != 0) {

    switch ((row % 2) != 0) {
        case true:
            console.log("The square is: Black!");
        break;
        default: console.log("The square is: White!");
    }

} else if ((column % 2) == 0) {

    switch ((row % 2) == 0) {
        case false:
            console.log("The square is: White!");
        break;
        default: console.log("The square is: Black!");
    }

}