import sys

def welcome_message():
    print("Simple Calculator")

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")

def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ('+', '-', '*', '/'):
            return operator
        else:
            print("Error: Unsupported operator. Please use one of +, -, *, /.")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return None
        else:
            return num1 / num2

def main():
    welcome_message()
    while True:
        first_number = get_number("Enter first number: ")
        operator = get_operator()
        second_number = get_number("Enter second number: ")

        result = calculate(first_number, second_number, operator)
        if result is not None:
            print(f"Result: {result}")
        
        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()