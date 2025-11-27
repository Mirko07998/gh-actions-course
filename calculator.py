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

def main():
    print("Simple Calculator")

    while True:
        try:
            first_number = input("Enter first number: ")
            first_number = float(first_number)
            
            operator = input("Enter operator (+, -, *, /): ")
            
            second_number = input("Enter second number: ")
            second_number = float(second_number)

            if operator == '+':
                result = add(first_number, second_number)
            elif operator == '-':
                result = subtract(first_number, second_number)
            elif operator == '*':
                result = multiply(first_number, second_number)
            elif operator == '/':
                result = divide(first_number, second_number)
            else:
                print("Error: Unsupported operator.")
                continue
            
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {str(e)}")
            continue

        repeat = input("Do you want to perform another calculation? (Y/N): ")
        if repeat.upper() != 'Y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()