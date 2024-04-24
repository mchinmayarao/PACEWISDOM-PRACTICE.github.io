
let displayValue = '';

function appendToDisplay(value) {
    displayValue += value;
    document.getElementById('display').value = displayValue;
}

function performOperation(operation) {
    displayValue += operation;
    document.getElementById('display').value = displayValue;
}

function calculateResult() {
    try {
        const result = eval(displayValue);
        document.getElementById('display').value = result;
        displayValue = result;
    } catch (error) {
        alert('Error in expression');
    }
}

function clearDisplay() {
    displayValue = '';
    document.getElementById('display').value = displayValue;
}

function toggleSign() {
    if (displayValue !== '') {
        if (displayValue.charAt(0) === '-') {
            displayValue = displayValue.slice(1);
        } else {
            displayValue = '-' + displayValue;
        }
        document.getElementById('display').value = displayValue;
    }
}


let memory = 0;

function addToMemory() {
    memory += parseFloat(displayValue);
}

function subtractFromMemory() {
    memory -= parseFloat(displayValue);
}

function recallMemory() {
    displayValue = memory.toString();
    document.getElementById('display').value = displayValue;
}

function clearMemory() {
    memory = 0;
}

function clearMemorySlot() {
    memory = 0;
}
