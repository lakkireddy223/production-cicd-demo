
# Production Ready CI/CD Flask Project

This project demonstrates a production-style CI/CD architecture.

## Technologies

- Flask
- Pytest
- GitHub Actions
- Docker
- Gunicorn
- Flake8

---

# Flow

Developer Push
    ↓
GitHub Actions
    ↓
Install Dependencies
    ↓
Code Quality Checks
    ↓
Automated Tests
    ↓
Docker Build
    ↓
Deployment Ready

---

# Important Files

## app/__init__.py

Contains Flask application factory.

Production applications use:

create_app()

Benefits:
- Better scalability
- Easier testing
- Cleaner structure

---

## tests/test_app.py

Automated test cases.

Used by CI pipeline.

---

## Dockerfile

Creates Docker container.

Industry standard deployment method.

---

## ci-cd.yml

Main CI/CD pipeline.

Steps:
1. Checkout code
2. Install Python
3. Install dependencies
4. Run flake8
5. Run tests
6. Build Docker image

---

# Run Project

## Install packages

pip install -r requirements.txt

---

## Run application

python run.py

---

## Run tests

python -m pytest

---

## Build Docker

docker build -t production-flask-app .

---

## Run Docker

docker run -p 5000:5000 production-flask-app
