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

def get_user_input():
    first_number = input("Enter the first number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    second_number = input("Enter the second number: ")
    return first_number, operator, second_number

def convert_to_number(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Error: Non-numeric value input.")

def main():
    print("Simple Calculator")
    while True:
        try:
            first_number_str, operator, second_number_str = get_user_input()
            first_number = convert_to_number(first_number_str)
            second_number = convert_to_number(second_number_str)

            result = perform_calculation(first_number, operator, second_number)
            print(f"Result: {result}")

        except ValueError as e:
            print(e)

        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()