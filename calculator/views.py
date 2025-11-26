```python
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def home(request):
    """Render the home page for the calculator."""
    return render(request, 'calculator/home.html')

@require_POST
def calculate(request):
    """Perform the calculation based on user input and return the result."""
    try:
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'undefined'
        else:
            result = 'Invalid Operation'

        return JsonResponse({'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)