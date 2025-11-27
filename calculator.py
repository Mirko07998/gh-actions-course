import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Simple Calculator")
    while True:
        try:
            first_number = input("Enter the first number: ")
            operator = input("Enter an operator (+, -, *, /): ")
            second_number = input("Enter the second number: ")

            # Convert inputs to numbers
            a = float(first_number)
            b = float(second_number)

            if operator == '+':
                result = add(a, b)
            elif operator == '-':
                result = subtract(a, b)
            elif operator == '*':
                result = multiply(a, b)
            elif operator == '/':
                result = divide(a, b)
            else:
                print("Error: Unsupported operator.")
                continue

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}. Please enter numeric values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Repeat usage
        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()