def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a numeric value.")

def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Error: Unsupported operator. Please use +, -, *, or /.")

def perform_calculation(first_num, operator, second_num):
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    elif operator == '*':
        return first_num * second_num
    elif operator == '/':
        if second_num == 0:
            print("Error: Cannot divide by zero.")
            return None
        return first_num / second_num

def main():
    print("Welcome to Simple Calculator!")
    while True:
        first_num = get_numeric_input("Enter first number: ")
        operator = get_operator()
        second_num = get_numeric_input("Enter second number: ")
        
        result = perform_calculation(first_num, operator, second_num)
        if result is not None:
            print(f"Result: {result}")

        repeat = input("Do you want to perform another calculation? (Y/N): ")
        if repeat.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()