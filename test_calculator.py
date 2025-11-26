import subprocess

def test_calculator_operations():
    # Test for addition
    assert calculate("1", "+", "1") == 2.0
    assert calculate("2", "-", "1") == 1.0
    assert calculate("2", "*", "3") == 6.0
    assert calculate("6", "/", "2") == 3.0

def test_calculator_error_handling():
    # Test for non-numeric value
    assert calculate("a", "+", "1") == "Error: Please enter numeric values for numbers."
    
    # Test for unsupported operator
    assert calculate("2", "&", "2") == "Error: Unsupported operator."
    
    # Test for division by zero
    assert calculate("4", "/", "0") == "Error: Cannot divide by zero."

# Helper function to simulate the calculator's calculation
def calculate(first_num, operator, second_num):
    try:
        first_num = float(first_num)
        second_num = float(second_num)

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
    except ValueError:
        return "Error: Please enter numeric values for numbers."