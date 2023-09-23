'use strict';

// let sum = 0

// while (true) {
//   let agePerson = prompt('Enter the age of each component of the group; after you entered all the ages, press enter to have the total price for your group');

//   if (agePerson === '') {
//     break;
//   }

//   if (agePerson <= 2) {
//     alert(0);
//   } else if (agePerson >= 3 && agePerson)
// }

let admissionPrice = 0;

while (true) {
    let agePerson = prompt(
        'Enter the age of each member of the group; after you entered all the ages, press enter to get the total price for your group'
    );

    if (agePerson === '') {
        break;
    }

    if (agePerson <= 2) {
        admissionPrice += 0; // No charge for children under 2
    } else if (agePerson >= 3 && agePerson <= 12) {
        admissionPrice += 14; // $14 charge for children aged 3-12
    } else if (agePerson >= 65) {
        admissionPrice += 18; // $18 charge for seniors aged 65 and over
    } else {
        admissionPrice += 23; // $23 charge for adults
    }
}

alert(`The total price for your group is: $${admissionPrice.toFixed(2)}`);
