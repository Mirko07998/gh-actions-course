```markdown
# Simple Calculator

This is a simple calculator web application built with Django. It supports basic arithmetic operations: addition, subtraction, multiplication, and division.
    
## Setup and Usage

### Prerequisites
Make sure you have [Python](https://www.python.org/downloads/) (version >= 3.12) and [Django](https://www.djangoproject.com/) installed.

### Getting Started
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd simple_calculator
   ```

2. Install requirements:
   ```bash
   pip install django
   ```

3. Run the migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the server:
   ```bash
   python manage.py runserver
   ```

5. Open your web browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

### Running Tests
To run the unit tests, use the following command:
```bash
python manage.py test calculator
```

### Notes
- Ensure that CSRF tokens are properly handled in your JavaScript.
- For division by zero, the application will return 'undefined'.

### Contributions
Feel free to contribute by submitting a pull request or filing an issue.