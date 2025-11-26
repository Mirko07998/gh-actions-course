import sys

def welcome_message():
    print("Welcome to the Simple Calculator")

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Error: Please enter a valid number.")

def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Error: Unsupported operator. Please enter one of +, -, *, /.")

def calculate(num1, operator, num2):
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
        num1 = get_number("Enter first number: ")
        operator = get_operator()
        num2 = get_number("Enter second number: ")

        result = calculate(num1, operator, num2)
        if result is not None:
            print(f"Result: {result}")

        again = input("Do you want to perform another calculation? (Y/N): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()