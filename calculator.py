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

def get_input(prompt):
    return input(prompt)

def perform_calculation(first_number, operator, second_number):
    if operator == '+':
        return add(first_number, second_number)
    elif operator == '-':
        return subtract(first_number, second_number)
    elif operator == '*':
        return multiply(first_number, second_number)
    elif operator == '/':
        return divide(first_number, second_number)
    else:
        raise ValueError("Error: Unsupported operator.")

def main():
    print("Simple Calculator")
    
    while True:
        try:
            first_input = get_input("Enter the first number: ")
            operator = get_input("Enter operator (+, -, *, /): ")
            second_input = get_input("Enter the second number: ")

            first_number = float(first_input)
            second_number = float(second_input)

            result = perform_calculation(first_number, operator, second_number)
            print(f"Result: {result}")

        except ValueError as e:
            print(e)
        
        repeat = get_input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat == 'N':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()