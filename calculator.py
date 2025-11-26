def main():
    print("Simple Calculator")
    
    while True:
        try:
            first_num = input("Enter the first number: ")
            operator = input("Enter an operator (+, -, *, /): ")
            second_num = input("Enter the second number: ")

            # Convert inputs to float
            first_num = float(first_num)
            second_num = float(second_num)

            # Perform calculation based on the operator
            if operator == '+':
                result = first_num + second_num
            elif operator == '-':
                result = first_num - second_num
            elif operator == '*':
                result = first_num * second_num
            elif operator == '/':
                if second_num == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = first_num / second_num
            else:
                print("Error: Unsupported operator.")
                continue

            # Print the result
            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter numeric values for numbers.")

        # Ask if user wants to perform another calculation
        repeat = input("Do you want to perform another calculation? (Y/N): ")
        if repeat.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()