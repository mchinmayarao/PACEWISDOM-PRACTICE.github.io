// function SandwichCalculator(bread){

//     return Math.floor(bread/2);
// }

// console.log(SandwichCalculator(13));

function SandwichCalculator(bread, cheese){

    var breadsForSandwich = Math.floor(bread/2);

    var totSandwich = (breadsForSandwich >= cheese)?cheese:breadsForSandwich;
    return totSandwich;
}

console.log(SandwichCalculator(2,16));