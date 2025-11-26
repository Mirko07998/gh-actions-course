```markdown
# Simple Calculator

## Overview
This is a simple web-based calculator application built using Django. It supports the basic operations: addition, subtraction, multiplication, and division.

## Prerequisites
Make sure you have Python 3.12 or higher installed on your machine.

## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages by running:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
1. Run the migrations:
   ```
   python manage.py migrate
   ```
2. Start the development server:
   ```
   python manage.py runserver
   ```
3. Open your browser and go to `http://127.0.0.1:8000/`.

## Usage
1. Enter the first number in the "Number 1" field.
2. Enter the second number in the "Number 2" field.
3. Choose an operation by selecting one of the radio buttons.
4. Click the "Calculate" button to view the result.

## Testing
To run the unit tests, execute:
```
python manage.py test
```
```