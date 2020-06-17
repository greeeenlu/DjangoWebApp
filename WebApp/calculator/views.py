from django.shortcuts import render


# Create your views here.
def calculator(request):
    content = {
        "displayResult": 4
    }
    return render(request, 'calculator/calculator.html', content)
