/*
# Compute the Perimeter of a Polygon

Write a program that computes the perimeter of a polygon. Begin by reading the x and y coordinates for the first point on the perimeter of the polygon from the user. Then continue reading pairs of values until the user enters a blank line for the x-coordinate. Each time you read an additional coordinate you should compute the distance to the previous point and add it to the perimeter. When a blank line is entered for the x-coordinate your program should add the distance from the last point back to the first point to the perimeter. Then the perimeter should be displayed. Sample input and output values are shown below. 
The input values entered by the user are shown in bold.

```
Enter the first x-coordinate: 0
Enter the first y-coordinate: 0
Enter the next x-coordinate (blank to quit): 1 Enter the next y-coordinate: 0
Enter the next x-coordinate (blank to quit): 0 Enter the next y-coordinate: 1
Enter the next x-coordinate (blank to quit):
The perimeter of that polygon is 3.414213562373095
```
*/

const prompt = require('prompt-sync')({sigint: true});

let coordinateX = Number(prompt("Inserisci la prima coordinata-X: => "));
let coordinateY = Number(prompt("Inserisci la prima coordinata-Y: => "));

const firstPointX = coordinateX;
const firstPointY = coordinateY;

let distance= 0;

while (true) {
    const nextX = prompt("Inserisci la prossima coordinata-X (PREMI INVIO SE HAI TERMINATO D'INSERIRE LE COORDINATE!): => ");
    if (nextX === "") {
        break;
    }
    const nextY = prompt("Inserisci la prossima coordinata-Y: => ");

    distance = Math.sqrt(Math.pow((nextX - coordinateX), 2) + Math.pow((nextY - coordinateY), 2)) + distance;

    coordinateX = nextX;
    coordinateY = nextY;

}

const lastPointDistance = Math.sqrt(Math.pow((coordinateX - firstPointX), 2) + Math.pow((coordinateY - firstPointY), 2));

const perimeter = lastPointDistance + distance;
console.log("Il perimetro del poligono è: " + perimeter);