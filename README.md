CONTENT:
# Simple Calculator Web App

## Overview
This is a simple calculator web application built using Django, which supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features
- Simple and functional user interface
- Basic arithmetic operations: +, -, *, /
- Error handling for invalid inputs

## Requirements
- Python >= 3.12
- Django >= 4.2

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd simple-calculator
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**
   ```bash
   pip install django
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   Open your web browser and visit `http://127.0.0.1:8000`.

## Unit Tests
To run the unit tests, execute the following command:
```bash
python manage.py test
```

## License
This project is licensed under the MIT License.