for (let i = 0; i < 100; i++ ) {

    let number = i +1;
    if (number % 3 === 0 && number % 5 === 0) {
        number = "fizz buzz";
    }
    else if (number % 5 === 0) {
        number = "buzz";
    }
    else if (number % 3 === 0) {
        number = "fizz";
    }
    
    console.log(number);
}