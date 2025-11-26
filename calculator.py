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

def get_operator_func(operator):
    operators = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    return operators.get(operator)

def main():
    print("Simple Calculator")

    while True:
        try:
            first_number = input("Enter the first number: ")
            operator = input("Enter an operator (+, -, *, /): ")
            second_number = input("Enter the second number: ")

            # Convert inputs to numbers
            num1 = float(first_number)
            num2 = float(second_number)

            # Get the correct function for the operator
            operation_func = get_operator_func(operator)
            if operation_func is None:
                print("Error: Unsupported operator.")
                continue

            # Perform the calculation
            result = operation_func(num1, num2)

            # Print the result
            print(f"Result: {result}")

        except ValueError as e:
            print(e)
        except Exception as e:
            print("An unexpected error occurred:", e)

        # Ask if the user wants to perform another calculation
        repeat = input("Do you want to perform another calculation? (Y/N): ")
        if repeat.strip().upper() != 'Y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()