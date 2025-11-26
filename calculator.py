def perform_calculation(first_num, operator, second_num):
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    elif operator == '*':
        return first_num * second_num
    elif operator == '/':
        if second_num == 0:
            return "Error: Cannot divide by zero."
        return first_num / second_num
    else:
        return "Error: Unsupported operator."

def main():
    print("Simple Calculator")
    
    while True:
        try:
            first_input = input("Enter first number: ")
            operator = input("Enter operator (+, -, *, /): ")
            second_input = input("Enter second number: ")
            
            first_num = float(first_input)
            second_num = float(second_input)

            result = perform_calculation(first_num, operator, second_num)

            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter a valid number.")
        
        cont = input("Do you want to perform another calculation? (Y/N): ").strip().lower()
        if cont != 'y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()