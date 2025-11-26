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

def get_number_input(prompt):
    while True:
        try:
            value = input(prompt)
            return float(value)  # convert input string to float
        except ValueError:
            print("Error: Please enter a valid number.")

def get_operator_input():
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ('+', '-', '*', '/'):
            return operator
        else:
            print("Error: Unsupported operator. Please use +, -, *, or /.")

def main():
    print("Simple Calculator")
    
    while True:
        first_number = get_number_input("Enter first number: ")
        operator = get_operator_input()
        second_number = get_number_input("Enter second number: ")
        
        try:
            if operator == '+':
                result = add(first_number, second_number)
            elif operator == '-':
                result = subtract(first_number, second_number)
            elif operator == '*':
                result = multiply(first_number, second_number)
            elif operator == '/':
                result = divide(first_number, second_number)

            print(f"Result: {result}")
        
        except ValueError as e:
            print(e)

        again = input("Do you want to perform another calculation (Y/N)? ").strip().upper()
        if again != 'Y':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()