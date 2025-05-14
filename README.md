# Widget API

This project is a simple RESTful API built with **Django** and **Django REST Framework** for managing `Widget` objects. It uses Django REST Framework's `ModelViewSet` to handle all CRUD operations, 
demonstrating how to build clean and maintainable REST APIs by leveraging DRF's built-in tooling.

## Features

- Full CRUD API for `Widgets`
- SQLite database persistence
- Django REST Framework serialization & validation
- Auto-managed `created_at` and `updated_at` fields
- Type annotations for maintainability
- Unit test coverage
- Linting with `flake8`
- Security scanning with `bandit`


## Tech Stack

- Python 3.8+
- Django 4.2 (LTS)
- Django REST Framework
- SQLite
- Django Test Client (via `APITestCase`)
- PEP8 compliance
- Bandit for static code analysis


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Eleven-Pigs/widget-api-assessment.git
cd widget-api
````

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations widgets
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at:
**[http://127.0.0.1:8000/widgets/](http://127.0.0.1:8000/widgets/)**



## 🧪 Run Tests

```bash
python manage.py test widgets
```

All core endpoints are tested under `widgets/tests.py`.

## Lint and Security Checks

### Run Linter (flake8)

```bash
flake8 .
```

### Run Security Scanner (bandit)

```bash
bandit -r .
```


## Widget Object Schema

```json
{
  "id": 1,
  "name": "Example Widget",
  "number_of_parts": 10,
  "created_at": "2025-05-13T12:34:56Z",
  "updated_at": "2025-05-13T12:34:56Z"
}
```
