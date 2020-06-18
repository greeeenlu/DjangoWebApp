from django.shortcuts import render


# Create your views here.
def calculator(request):
    content = {
        "displayResult": 0
    }
    if request.method == 'POST':
        form = request.POST
        print(form)
        if 'digitalInput' in form:
            content['displayResult'] = form['digitalInput']
    return render(request, 'calculator/calculator.html', content)
