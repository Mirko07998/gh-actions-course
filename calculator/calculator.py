import sys

def welcome_message():
    print("Welcome to Simple Calculator")

def get_user_input():
    first_number = input("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ")
    second_number = input("Enter second number: ")
    return first_number, operator, second_number

def calculate(first_number, operator, second_number):
    try:
        num1 = float(first_number)
        num2 = float(second_number)

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
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."

def main():
    welcome_message()
    
    while True:
        first_number, operator, second_number = get_user_input()
        result = calculate(first_number, operator, second_number)
        print(f"Result: {result}")
        
        another_calculation = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if another_calculation != 'Y':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()