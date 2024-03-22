var brackets = '[[[[[]]]]]'

function measureDepth(brackets){

    return brackets.length/2
}

console.log(measureDepth(brackets));