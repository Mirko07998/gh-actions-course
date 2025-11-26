import subprocess

def test_calculator_operations():
    # Testing addition
    result = run_calculator('5', '+', '3')
    assert result == "Result: 8.0"

    # Testing subtraction
    result = run_calculator('10', '-', '4')
    assert result == "Result: 6.0"

    # Testing multiplication
    result = run_calculator('7', '*', '6')
    assert result == "Result: 42.0"

    # Testing division
    result = run_calculator('20', '/', '4')
    assert result == "Result: 5.0"

    # Testing division by zero
    result = run_calculator('5', '/', '0')
    assert result == "Error: Cannot divide by zero."

    # Testing invalid operator
    result = run_calculator('5', '%', '3')
    assert result == "Error: Unsupported operator."

def run_calculator(first_num, operator, second_num):
    process = subprocess.Popen(['python', 'calculator.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=f"{first_num}\n{operator}\n{second_num}\nY\n".encode())
    return stdout.decode().strip().split('\n')[-1]

if __name__ == "__main__":
    test_calculator_operations()