from django.shortcuts import render, redirect



# Create your views here.
def calculator(request, result='0'):
    content = {
        'result' : result
    }
    return  render(request, 'calculator/calculator.html', content)

def digitInput(request, digit, previous):
    if previous == '0':
        newResult = str(digit)
    else:
        newResult = previous + str(digit)

    return redirect(calculator,result=newResult )


