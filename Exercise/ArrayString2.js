var str = "the quick brown fox";

function latinConverter(str){

    strArray = str.split(' ');
   // console.log(strArray);
    var latinString = []
    strArray.forEach(element => {
        
        var elementArray = element.split('');
        var first = elementArray.shift();
        elementArray.push(first,'ay');
        latinString.push(elementArray.join(''));
        
    });

    return latinString.join(" ");
}

console.log(latinConverter(str));