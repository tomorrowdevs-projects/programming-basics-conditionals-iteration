/* 
In this exercise you will create a program that reads a letter of the alphabet from the user.  
If the user enters **a, e, i, o or u** then your program should display a message
indicating that the entered letter is a **vowel**.  
If the user enters **y** then your program should display a message
indicating that **sometimes y is a vowel, and sometimes y is a consonant**.  
Otherwise, your program should display a message indicating that **the letter is a consonant**.
*/

let letter = prompt ('Write a letter of the alphabet');

if(letter === 'a'){
  console.log("The Letter 'a' is a vowel")
}else if(letter === 'e'){
  console.log("The Letter 'e' is a Vowel")
}else if(letter === 'i'){
  console.log("The Letter 'i' is a Vowel")
}else if(letter === 'o'){
  console.log ("The Letter 'o' is a Vowel")
}else if(letter === 'u'){
  consolo.log("The Letter 'u' is a Vowel")
}else if(letter === 'y'){
  console.log(" 'y' sometimes is a Vowel, and sometimes 'Y' is a Consonant")
}else{
  console.log("The letter is a Consonat ")
}
 