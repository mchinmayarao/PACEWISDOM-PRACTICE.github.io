// __proto__
const obj = {};
console.log(obj.__proto__);

// JS Recursion
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(5));

// Curry Functions
const add = x => y => x + y;
const add5 = add(5);
console.log(add5(3));

// Shallow Copy
const original = { a: 1, b: { c: 2 } };
const shallowCopy = Object.assign({}, original);

// Pure Functions
function add(x, y) {
  return x + y;
}

// IIFE (Immediately Invoked Function Expression)
(function() {
  console.log('IIFE executed');
})();

// Function Expression
const multiply = function(x, y) {
  return x * y;
};

// Composition over Inheritance
const compose = (f, g) => x => f(g(x));

// Pipe Functions
const pipe = (...functions) => input => functions.reduce((acc, fn) => fn(acc), input);

// Compose Functions
const composeFunctions = compose(
  add5,
  multiply
);

// Debouncing Function
function debounce(func, delay) {
  let timeoutId;
  return function() {
    const context = this;
    const args = arguments;
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(context, args), delay);
  };
}

// Throttling Function
function throttle(func, limit) {
  let inThrottle;
  return function() {
    const context = this;
    const args = arguments;
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Async/Await
async function fetchData() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Call the examples
console.log(composeFunctions(3, 4)); // Should output 35
const debouncedFunc = debounce(() => console.log('Debounced function executed'), 500);
const throttledFunc = throttle(() => console.log('Throttled function executed'), 1000);

// You can call other examples or test functions as needed.
