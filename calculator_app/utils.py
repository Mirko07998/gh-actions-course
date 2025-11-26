def calculate(first_number: float, operator: str, second_number: float) -> float:
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return first_number / second_number
    else:
        raise ValueError("Unsupported operator. Please use +, -, *, or /.")