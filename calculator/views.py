CONTENT:
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'calculator/home.html')

def calculate(request):
    if request.method == 'GET':
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')
        operation = request.GET.get('operation')

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Error: Invalid operation"

            return JsonResponse({'result': result})
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid input'})