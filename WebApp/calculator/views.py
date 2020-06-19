from django.shortcuts import render

def calculator(request):
    def initContent():
        return {
            'displayResult': 0,
            'lastOperator': '=',
            'previousValue': 0,
            'newValue': 0,
            'isOperatorClicked': False
        }
    content = initContent()
    if request.method == 'POST':
        form = request.POST
        print('FORM : ' + str(form))

        if 'newValue' in form:
            content['newValue'] = int(form['newValue'])
        if 'previousValue' in form:
            content['previousValue'] = int(form['previousValue'])
        if 'lastOperator' in form:
            content['lastOperator'] = form['lastOperator']
        if 'isOperatorClicked' in form:
            content['isOperatorClicked'] = form['isOperatorClicked']
        if 'operatorInput' in form:
            if content['isOperatorClicked'] == 'True':
                content['lastOperator'] = form['operatorInput']
                content['displayResult'] = content['previousValue']
                return render(request, 'calculator/calculator.html', content)

            if content['isOperatorClicked'] == 'False':
                content['isOperatorClicked'] = True

            operate = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                'x': lambda x, y: x * y,
                '÷': lambda x, y: x // y,
            }
            if content['lastOperator'] == '=':
                content['previousValue'] = content['newValue']
                content['displayResult'] = content['previousValue']
            else:
                try:
                    newValue = operate[content['lastOperator']](int(form['previousValue']), int(form['newValue']))
                except:
                    content = initContent()
                    content['alert'] = True
                    print('CONTENT: ' + str(content))
                    return render(request, 'calculator/calculator.html', content)
                content['displayResult'] = newValue
                content['previousValue'] = newValue
            content['lastOperator'] = form['operatorInput']
            content['newValue'] = 0

        if 'digitalInput' in form:
            content['isOperatorClicked'] = False
            newValue = content['newValue'] * 10 + int(form['digitalInput'])
            if newValue > 9999999999999:
                content['displayResult'] = content['newValue']
                return render(request, 'calculator/calculator.html', content)
            else:
                content['displayResult'] = newValue
                content['newValue'] = newValue
        print('CONTENT: ' + str(content))
    return render(request, 'calculator/calculator.html', content)
