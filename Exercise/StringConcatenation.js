var greeting = "Hello";
var name = "world";
var full = greeting +" " + name;
full = full.replace(/l/g, 1);
full = full.replace(/o/g, 0);
console.log(full);

function reverseString(s){
    return s.split('').reverse().join('');
}

console.log(reverseString(full));