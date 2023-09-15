'use strict';

let firstXCoordinate = parseFloat(prompt('Enter the first x-coordinate'));
let firstYCoordinate = parseFloat(prompt('Enter the first y-coordinate'));
let counter = 0;
let distanceLastPoint;

let nextXCoordinate = parseFloat(
    prompt('Enter the next x-coordinate (blank to quit')
);
let nextYCoordinate = parseFloat(prompt('Enter the next y-coordinate'));

let distanceFirstPoint = Math.sqrt;
Math.pow(firstXCoordinate - nextXCoordinate, 2) +
    Math.pow(firstYCoordinate - nextYCoordinate, 2);

while (nextXCoordinate !== ' ') {
    if (true) {
        console.log(distanceFirstPoint);
        let nextXCoordinate = parseFloat(
            prompt('Enter the next x-coordinate (blank to quit')
        );
        let nextYCoordinate = parseFloat(prompt('Enter the next y-coordinate'));

        let distanceOtherPoint = console.log(
            `${Math.sqrt(
                Math.pow(nextXCoordinate - nextXCoordinate, 2) +
                    Math.pow(nextYCoordinate - nextYCoordinate, 2)
            )}`
        );
        counter++;
    } else {
        distanceLastPoint = console.log(
            `${Math.sqrt(
                Math.pow(nextXCoordinate - firstXCoordinate, 2) +
                    Math.pow(nextYCoordinate - firstYCoordinate, 2)
            )}`
        );
        break;
    }
}
