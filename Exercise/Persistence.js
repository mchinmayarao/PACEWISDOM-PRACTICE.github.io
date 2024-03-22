var num = 9989;

var count = 0;

function Persistence(num) {
    var numStr = ("" + num).split('');

    if (numStr.length == 1) {
        return 0;
    }
    var numInt = numStr.map(parseFloat);
    // console.log(numInt);

    var prd = numInt.reduce((a, b) => a * b);

    console.log(numStr.join(" * ") + ' = ' + prd);

    count = count + 1;
    Persistence(prd);
    return count;




}

console.log("Multiplicative Persistence of", num, "is:", Persistence(num));



