def perform_calculation(first_number, operator, second_number):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        if second_number == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return first_number / second_number
    else:
        raise ValueError("Error: Unsupported operator.")

def main():
    print("Simple Calculator")
    while True:
        try:
            first_input = input("Enter the first number: ")
            first_number = float(first_input)

            operator = input("Enter an operator (+, -, *, /): ")

            second_input = input("Enter the second number: ")
            second_number = float(second_input)

            result = perform_calculation(first_number, operator, second_number)
            print(f"Result: {result}")

        except ValueError as e:
            print(e)

        again = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()