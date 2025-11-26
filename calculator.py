def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Error: Please enter a numeric value.")

def get_operator(prompt):
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input(prompt)
        if operator in valid_operators:
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
        return num1 / num2

def main():
    print("Simple Calculator")
    
    while True:
        num1 = get_number("Enter the first number: ")
        operator = get_operator("Enter an operator (+, -, *, /): ")
        num2 = get_number("Enter the second number: ")
        
        result = calculate(num1, operator, num2)
        if result is not None:
            print(f"Result: {result}")
        
        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()