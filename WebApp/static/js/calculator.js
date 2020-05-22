alert("this is calculator");

var result = document.getElementById('result');
var previousValue = 0; 
var newValue = 0;
var lastOperator = ''

function inputDigit(x){
    if(result.innerText.length >= 14) return;

    if (result.innerText == '0' || newValue == 0){
        result.innerText = x;
    }else{
        result.innerText += x;
    }

    newValue = parseInt(result.innerText);
    console.log('newValue:' + newValue);
}

function inputOperator(operator){
    console.log("lastOperator", lastOperator, lastOperator.length );
    if(lastOperator.length == 0) {
        previousValue = newValue;
    }
    calculate(lastOperator);
    newValue = 0
    lastOperator = operator;
}

function calculate(operator){
    switch (operator) {
        case 'plus':
            result.innerText = previousValue + newValue;
            break;
        case 'minus':
            result.innerText = previousValue - newValue;
            break;
        case 'times':
            result.innerText = previousValue * newValue;
            break;
        case 'divide':
            result.innerText = previousValue / newValue;
            break;
        default:
            break;
    }

    previousValue = parseInt(result.innerText);
}