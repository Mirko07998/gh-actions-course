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

def get_numeric_input(prompt):
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Error: Please enter a numeric value.")

def main():
    print("Simple Calculator")

    while True:
        # User input
        first_number = get_numeric_input("Enter the first number: ")
        operator = input("Enter an operator (+, -, *, /): ")
        second_number = get_numeric_input("Enter the second number: ")

        # Processing
        try:
            if operator == '+':
                result = add(first_number, second_number)
            elif operator == '-':
                result = subtract(first_number, second_number)
            elif operator == '*':
                result = multiply(first_number, second_number)
            elif operator == '/':
                result = divide(first_number, second_number)
            else:
                print("Error: Unsupported operator.")
                continue

            # Output result
            print(f"Result: {result}")

        except ValueError as e:
            print(e)

        # Repeat usage
        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()