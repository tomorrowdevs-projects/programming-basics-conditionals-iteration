/*
A particular zoo determines the price of admission based on the age of the guest.

1) Guests 2 years of age and less are admitted without charge.
Children between 3 and 12 years of age cost $14.00.
Seniors aged 65 years and over cost $18.00.
Admission for all other guests is $23.00.
2) Create a program that begins by reading the ages of all the guests in a group from the user, with one age entered on each line.

3) The user will enter a blank line (a newline character) to indicate that there are no more guests in the group.

4)Then your program should display the admission cost for the group with an appropriate message.

5) The cost should be displayed using two decimal places.
*/

let costAdmission = 0;

while (true) {
    const userAge = prompt(
        `Enter the age of each components of the group. If the group is finished, press enter`
    );

    if (userAge === ' ') {
        break;
    }
}

const age = parseInt(userAge);

let costPerson = 0;

if (age <= 2) {
    costPerson = 0.0;
} else if (age >= 3 && age <= 12) {
    costPerson = 14.0;
} else if (age >= 65) {
    costPerson = 18.0;
} else {
    costPerson = 23.0;
}

costAdmission += costPerson;

alert(`The total cost for the group is: ${costAdmission.toFixed(2)}`);
