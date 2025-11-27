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
            first_num = input("Enter the first number: ")
            operator = input("Enter the operator (+, -, *, /): ")
            second_num = input("Enter the second number: ")
            
            # Convert inputs to floats
            first_num = float(first_num)
            second_num = float(second_num)

            # Perform the operation based on the operator
            if operator == '+':
                result = add(first_num, second_num)
            elif operator == '-':
                result = subtract(first_num, second_num)
            elif operator == '*':
                result = multiply(first_num, second_num)
            elif operator == '/':
                result = divide(first_num, second_num)
            else:
                print("Error: Unsupported operator.")
                continue

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {str(e)}")
            continue

        should_continue = input("Do you want to perform another calculation? (Y/N): ")
        if should_continue.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()