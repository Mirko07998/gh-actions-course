from django.shortcuts import render
from .utils import calculate

def calculator_view(request):
    result = None
    error = None

    if request.method == 'POST':
        num1 = request.POST.get('num1')
        operator = request.POST.get('operator')
        num2 = request.POST.get('num2')

        try:
            result = calculate(num1, operator, num2)
        except ValueError as e:
            error = str(e)

    return render(request, 'calculator/index.html', {'result': result, 'error': error})