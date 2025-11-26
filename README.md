CONTENT:
# Simple Calculator Web App

This project contains a simple calculator web application built using Django. It supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Prerequisites

- Python 3.12 or higher
- pip
- Django
- Uvicorn (for running the server)

## Installation

1. Clone the repository:
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations (if needed):
   ```bash
   python manage.py migrate
   ```

5. Start the server using Uvicorn:
   ```bash
   uvicorn simple_calculator.asgi:application --host 127.0.0.1 --port 8000
   ```

6. Open your browser and go to `http://127.0.0.1:8000/` to use the calculator.

## Usage

Simply enter numbers and select an operation. Press "Calculate" to view the result. The calculator supports the following operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

The application performs basic error handling, ensuring that division by zero is caught and handled gracefully.

## Running Tests

To run the unit tests, run the following command:
```bash
python manage.py test calculator
```