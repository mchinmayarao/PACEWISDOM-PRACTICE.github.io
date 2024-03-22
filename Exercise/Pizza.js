var toppings = ['Cheese','tomatoes','ham', 'bits'];



function makePizza(toppings){
    return "A tasty pizza with " + toppings.join(' and ');
}

console.log(makePizza(toppings));