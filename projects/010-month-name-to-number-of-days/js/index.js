//Begin by writing a program that **reads the name of a note** from the user and **displays the note’s frequency**.  
//Your program should support all the notes listed previously.

const noteName = prompt("Write the name of the note");
console.log(`Input = ${noteName}`)


if (noteName === "c4"){
  console.log("Frequency = 261.63 Hz")
}else if(noteName === "c0"){
  c0 = 32.7 / 2;
  console.log(`Frequency = ${c0.toFixed(2)}Hz`)
}else if (noteName === "c1"){
  c1 = 65.4 / 2;
  console.log(`Frequency = ${c1.toFixed(2)}Hz`)
}else if (noteName === "c2"){
  c2 = 130.81 / 2;
  console.log(`Frequency = ${c2.toFixed(2)}Hz`)
}else if(noteName === "c3"){
  c3 = 261.63 / 2;
  console.log(`Frequency = ${c3.toFixed(2)}Hz`)
}else if(noteName ==="c5"){
  const c5 = 261.63 * 2;
  console.log(`Frequency = ${c5.toFixed(2)}Hz`);
}else if(noteName === "c6"){
  c6 = 523.26 * 2;
  console.log(`Frequency = ${c6.toFixed(2)}Hz`);
}else if (noteName === "c7"){
  c7 = 1046.52 * 2;
  console.log(`Frequency = ${c7.toFixed(2)}Hz`) 
}else if (noteName === "c8"){
  c8 = 2093 * 2;
  console.log(`Frequency = ${c8.toFixed(2)}Hz`)

  
}else if(noteName === "d4"){
  console.log("Frequency = 293.66Hz");
}else if(noteName === "e4"){
  console.log("Frequency = 329.63Hz");
}else if(noteName === "f4"){
  console.log("Frequency = 349.23Hz");
}else if(noteName === "g4"){
  console.log("Frequency = 392Hz");
}else if(noteName === "a4"){
  console.log("Frequency = 440Hz");
}else if(noteName === "b4"){
  console.log("Frequency = 493.88Hz");
}