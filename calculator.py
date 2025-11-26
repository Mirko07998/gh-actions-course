import sys

def welcome():
    print("Simple Calculator")

def get_input():
    first_number = input("Enter the first number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    second_number = input("Enter the second number: ")
    return first_number, operator, second_number

def perform_operation(first_number, operator, second_number):
    try:
        num1 = float(first_number)
        num2 = float(second_number)
    except ValueError:
        return "Error: Please enter valid numeric values."

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Error: Unsupported operator."

def main():
    welcome()
    while True:
        first_number, operator, second_number = get_input()
        result = perform_operation(first_number, operator, second_number)
        print(f"Result: {result}")
        
        again = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if again != 'Y':
            break
    
    print("Goodbye!")
    sys.exit()

if __name__ == "__main__":
    main()