//The length of a month varies from 28 to 31 days.  
//In this exercise you will create a program that reads **the name of a month** from the user as a string.  
//Then your program should display the number of days in that month.  
//Display **28 or 29 days** for **February** so that leap years are addressed.

const month = prompt("Write a month like:'March' ");

if (month === "Jenuary"){
    console.log(`${month} as 31 days`)   
}else if (month === "February"){
    console.log(`${month} as 28 days`)
}else if (month === "March"){
    console.log(`${month} as 31 days`)
}else if (month === "April") {
    console.log(`${month} as 30 days`)
}else if (month === "May") {
    console.log(`${month} as 31 days`)
}else if (month === "June") {
    console.log(`${month} as 30 days`)
}else if (month === "July") {
    console.log(`${month} as 31 days`)
}else if (month === "August") {
    console.log(`${month} as 31 days`)
}else if (month === "September") {
    console.log(`${month} as 30 days`)
}else if (month === "October") {
    console.log(`${month} as 31 days`)
}else if (month === "November") {
    console.log(`${month} as 30 days`)
}else if (month === "Dicembre") {
    console.log(`${month} as 31 days`)
}else {
    console.log("You enter a wronge month")
} 