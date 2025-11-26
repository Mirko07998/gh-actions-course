# Simple Calculator

This is a simple calculator application that can perform basic arithmetic operations including addition, subtraction, multiplication, and division.

## Running the Application

To run the application, use the following command in the terminal:

```
python calculator.py
```

## Features

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

## Error Handling

The application will handle the following errors gracefully:
- Non-numeric input will prompt an error message without crashing.
- Input of an unsupported operator will notify the user.
- An attempt to divide by zero will provide a relevant error message.

## Running Tests

To run the tests, use the following command:

```
python -m unittest test_calculator.py
```

## Exit

The application will terminate gracefully with a "Goodbye!" message.