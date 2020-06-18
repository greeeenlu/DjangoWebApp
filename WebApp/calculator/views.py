from django.shortcuts import render


# Create your views here.
def calculator(request):
    content = {
        'displayResult': 0,
        'lastOperator': '=',
        'previousValue': 0,
        'newValue': 0,
        'isOperatorClicked': False
    }
    if request.method == 'POST':
        form = request.POST
        print(form)
        if 'newValue' in form:
            content['newValue'] = int(form['newValue'])
        if 'previousValue' in form:
            content['previousValue'] = int(form['previousValue'])
        if 'lastOperator' in form:
            content['lastOperator'] = form['lastOperator']
        if 'operatorInput' in form:
            operate = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                'x': lambda x, y: x * y,
                '÷': lambda x, y: x // y,
            }
            if content['lastOperator'] == '=':
                content['previousValue'] = content['newValue']
                content['displayResult'] = content['newValue']
            else:
                newValue = operate[content['lastOperator']](int(form['previousValue']), int(form['newValue']))
                print('operatorInput : newinput:' + str(newValue))
                content['displayResult'] = newValue
                content['previousValue'] = newValue
            content['lastOperator'] = form['operatorInput']
            content['newValue'] = 0

        if 'digitalInput' in form:
            newValue = content['newValue'] * 10 + int(form['digitalInput'])
            print(newValue)
            if newValue > 9999999999999:
                content['displayResult'] = content['newValue']
                return render(request, 'calculator/calculator.html', content)
            else:
                content['displayResult'] = newValue
                content['newValue'] = newValue
        print(content)
    return render(request, 'calculator/calculator.html', content)
