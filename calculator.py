import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error: Cannot divide by zero.")
    return x / y

def get_input():
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))
        return first_number, operator, second_number
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None, None, None

def calculate(first_number, operator, second_number):
    if operator == '+':
        return add(first_number, second_number)
    elif operator == '-':
        return subtract(first_number, second_number)
    elif operator == '*':
        return multiply(first_number, second_number)
    elif operator == '/':
        return divide(first_number, second_number)
    else:
        raise ValueError("Error: Unsupported operator.")

def main():
    print("Simple Calculator")
    while True:
        first_number, operator, second_number = get_input()
        if first_number is None:
            continue
        
        try:
            result = calculate(first_number, operator, second_number)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)

        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            print("Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()