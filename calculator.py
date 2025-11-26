def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a numeric value.")

def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in valid_operators:
            return operator
        else:
            print("Error: Unsupported operator. Please enter one of +, -, *, /.")

def calculate(first_number, operator, second_number):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        if second_number == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return first_number / second_number

def main():
    print("Simple Calculator")
    
    while True:
        first_number = get_number("Enter first number: ")
        operator = get_operator()
        second_number = get_number("Enter second number: ")

        try:
            result = calculate(first_number, operator, second_number)
            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(e)

        cont = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if cont != 'Y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()