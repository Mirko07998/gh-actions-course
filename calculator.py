def main():
    print("Simple Calculator")
    
    while True:
        try:
            first_number = input("Enter the first number: ")
            operator = input("Enter an operator (+, -, *, /): ")
            second_number = input("Enter the second number: ")

            # Convert input strings to float
            first_number = float(first_number)
            second_number = float(second_number)

            if operator == '+':
                result = first_number + second_number
            elif operator == '-':
                result = first_number - second_number
            elif operator == '*':
                result = first_number * second_number
            elif operator == '/':
                if second_number == 0:
                    raise ValueError("Error: Cannot divide by zero.")
                result = first_number / second_number
            else:
                raise ValueError("Error: Unsupported operator. Please use +, -, *, or /.")

            print(f"Result: {result}")

        except ValueError as e:
            print(e)

        again = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if again != 'Y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()