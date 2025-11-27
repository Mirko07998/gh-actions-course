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

def get_user_input():
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))
        return first_number, operator, second_number
    except ValueError:
        print("Error: Please enter numeric values.")
        return None, None, None

def calculate(first_number, operator, second_number):
    if operator == "+":
        return add(first_number, second_number)
    elif operator == "-":
        return subtract(first_number, second_number)
    elif operator == "*":
        return multiply(first_number, second_number)
    elif operator == "/":
        return divide(first_number, second_number)
    else:
        print("Error: Unsupported operator.")
        return None

def main():
    print("Simple Calculator")
    while True:
        first_number, operator, second_number = get_user_input()
        if first_number is None or operator is None or second_number is None:
            continue

        result = calculate(first_number, operator, second_number)
        if result is not None:
            print(f"Result: {result}")

        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()