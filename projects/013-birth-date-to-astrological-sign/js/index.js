'use strict';
// Read imput from the user
const monthInput = prompt('Enter the month in which you were born');
const dayInput = parseFloat(prompt('Enter the day you were born'));

// All the possible combinations
if (monthInput === 'December') {
    if (dayInput >= 22) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Capricorn`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Sagittarius`
        );
    }
}

if (monthInput === 'January') {
    if (dayInput >= 20) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Aquarius`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Capricorn`
        );
    }
}

if (monthInput === 'February') {
    if (dayInput >= 19) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Pisces`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Aquarius`
        );
    }
}

if (monthInput === 'March') {
    if (dayInput >= 21) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Aries`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Pisces`
        );
    }
}

if (monthInput === 'April') {
    if (dayInput >= 20) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Taurus`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Aries`
        );
    }
}

if (monthInput === 'May') {
    if (dayInput >= 21) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Gemini`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Taurus`
        );
    }
}

if (monthInput === 'June') {
    if (dayInput >= 21) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Cancer`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Gemini`
        );
    }
}

if (monthInput === 'Juli') {
    if (dayInput >= 23) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Leo`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Cancer`
        );
    }
}

if (monthInput === 'August') {
    if (dayInput >= 23) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Virgo`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Leo`
        );
    }
}

if (monthInput === 'September') {
    if (dayInput >= 23) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Libra`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Virgo`
        );
    }
}

if (monthInput === 'October') {
    if (dayInput >= 23) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Scorpio`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Libra`
        );
    }
}

if (monthInput === 'November') {
    if (dayInput >= 22) {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Sagittarius`
        );
    } else {
        alert(
            `Month input = ${monthInput}; Day input: ${dayInput}; Output: Scorpio`
        );
    }
}
