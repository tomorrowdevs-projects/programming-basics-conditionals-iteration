let flipsAverage = 0;

for (let i = 0; i < 10; i++) {
    let series = "";

    let counter = 0;
    while (true) {
        let coinFace = Math.floor((Math.random() * 2) + 1);

        switch (coinFace) {
            case 1:
                coinFace = "H";
            break;
            default:
                coinFace = "T";
        }
        series = series + coinFace;
        counter++;

        if (series.length >= 3 && series[series.length - 1] == series[series.length - 2] && series[series.length - 2] == series[series.length - 3]) {
            
            console.log(series + " (" + counter +" flips!)");
            flipsAverage = flipsAverage + counter;
            break;
            
        }
    }
}

console.log("In media sono stati necessari " + (flipsAverage/10) + " flips, per ottenere 3 facce uguali consecutive!\n");

