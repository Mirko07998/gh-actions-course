def main():
    print("Simple Calculator")
    
    while True:
        try:
            # User Input
            first_num = input("Enter the first number: ")
            operator = input("Enter the operator (+, -, *, /): ")
            second_num = input("Enter the second number: ")

            # Convert inputs to numeric values
            first_num = float(first_num)
            second_num = float(second_num)

            # Perform calculation based on the operator
            if operator == "+":
                result = first_num + second_num
            elif operator == "-":
                result = first_num - second_num
            elif operator == "*":
                result = first_num * second_num
            elif operator == "/":
                if second_num == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = first_num / second_num
            else:
                print("Error: Unsupported operator.")
                continue

            # Output the result
            print(f"Result: {result}")
        
        except ValueError:
            print("Error: Please enter numeric values only.")
        
        # Check if the user wants to perform another calculation
        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()