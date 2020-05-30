from django.shortcuts import render, redirect

operate = {
        'plus': lambda x, y: x + y,
        'minus': lambda x, y: x - y,
        'times': lambda x, y: x * y,
        'divide': lambda x, y: x // y,
    }
DISPLAY_MAX_LENGTH = 14

def calculator(request, newResult='0', lastResult='0', lastOperator='equals', reset=1):
    content = {
        'newResult' : newResult,
        'lastResult' : lastResult,
        'lastOperator' : lastOperator,
        'reset': reset,
    }
    return  render(request, 'calculator/calculator.html', content)

def digitInput(request, digit, previous, lastResult, lastOperator, reset):
    global DISPLAY_MAX_LENGTH
    if reset:
        newResult = str(digit)
    elif len(previous) >= DISPLAY_MAX_LENGTH:
        newResult = previous
    else:
        newResult = previous + str(digit)

    return redirect(calculator,newResult=newResult,lastResult=lastResult, lastOperator=lastOperator, reset=0)

def operatorInput(request, operator, newResult, lastResult, lastOperator, reset):
    global operate
    if reset:
        return redirect(calculator,newResult=newResult,lastResult=lastResult, lastOperator=operator, reset=1)
    elif lastOperator === 'equals':
        return redirect(calculator,newResult=newResult,lastResult=newResult, lastOperator=operator, reset=1)
    else:
        result = operate[lastOperator](int(lastResult),int(newResult))
    return redirect(calculator,newResult=result,lastResult=result, lastOperator=operator, reset=1)



