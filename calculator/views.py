```python
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'calculator/home.html')

def calculate(request):
    if request.method == 'GET':
        try:
            num1 = float(request.GET.get('num1', 0))
            num2 = float(request.GET.get('num2', 0))
            operation = request.GET.get('operation', '')
            result = 0

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return JsonResponse({'error': 'Division by zero is not allowed.'}, status=400)
            else:
                return JsonResponse({'error': 'Invalid operation.'}, status=400)

            return JsonResponse({'result': result})
        except ValueError:
            return JsonResponse({'error': 'Invalid input, please enter numbers only.'}, status=400)

    return JsonResponse({'error': 'GET request required.'}, status=400)
```