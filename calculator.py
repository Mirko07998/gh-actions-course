import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def get_number(prompt):
    while True:
        input_str = input(prompt)
        try:
            return float(input_str)
        except ValueError:
            print("Error: Please enter a numeric value.")

def get_operator():
    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        if operator in ('+', '-', '*', '/'):
            return operator
        else:
            print("Error: Unsupported operator. Please use +, -, * or /.")

def calculate():
    print("Simple Calculator")
    
    while True:
        num1 = get_number("Enter first number: ")
        operator = get_operator()
        num2 = get_number("Enter second number: ")

        try:
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)

            print(f"Result: {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")

        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat == 'N':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    calculate()