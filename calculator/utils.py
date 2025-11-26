def calculate(num1: str, operator: str, num2: str):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError("Please enter valid numbers.")

    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operator selected.")

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return num1 / num2