'use strict';

/*What Color Is That Square?
Positions on a chess board are identified by a letter and a number.
The letter identifies the column, while the number identifies the row, as shown below:



1) Write a program that reads a position from the user.

2) Use an if statement to determine if the column begins with a black square or a white square.

3) Then use modular arithmetic to report the color of the square in that row. Your program may assume that a valid position will always be entered. It does not need to perform any error checking.*/

// Read input from the user
const getColumns = prompt('Enter a letter between a and h'.toLowerCase());
const getRows = parseFloat(prompt('Enter a number between 1 and 8'));

// Create a solution with the remainder. toLowerCase to convert in lower case the getColumns
if (
    ((getColumns === 'a' ||
        getColumns === 'c' ||
        getColumns === 'e' ||
        getColumns === 'g') &&
        getRows % 2 === 1) ||
    ((getColumns === 'b' ||
        getColumns === 'd' ||
        getColumns === 'f' ||
        getColumns === 'h') &&
        getRows % 2 === 0)
) {
    alert(`Input = ${getColumns.toUpperCase()}${getRows}; Output = black`);
} else {
    alert(`Input = ${getColumns.toUpperCase()}${getRows}; Output = white`);
}
