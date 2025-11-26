def main():
    print("Simple Calculator")
    
    while True:
        try:
            first_number = input("Enter the first number: ")
            operator = input("Enter an operator (+, -, *, /): ")
            second_number = input("Enter the second number: ")

            # Convert input strings to floats
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
                    print("Error: Cannot divide by zero.")
                    continue
                result = first_number / second_number
            else:
                print("Error: Unsupported operator.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter numeric values.")
            continue
        
        # Check if user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if another_calculation != 'Y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()