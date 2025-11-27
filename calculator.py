def main():
    print("Simple Calculator")
    while True:
        try:
            first_num = input("Enter the first number: ")
            operator = input("Enter an operator (+, -, *, /): ")
            second_num = input("Enter the second number: ")

            first_num = float(first_num)
            second_num = float(second_num)

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

            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        repeat = input("Do you want to perform another calculation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()