# Bookstore API

## Overview
The Bookstore API provides a comprehensive solution for managing a bookstore's inventory, customers, orders, and other related functionalities using Django and PostgreSQL. It enables users to interact with the bookstore database, perform CRUD operations on books, manage customer data, process orders, and more.

## Table of Contents
1. [Getting Started](#getting-started)
2. [API Endpoints](#api-endpoints)
3. [Authentication](#authentication)
4. [Request and Response Formats](#request-and-response-formats)
5. [Error Handling](#error-handling)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)

## Getting Started

### Prerequisites
- Python 3.8+
- Django
- Django REST framework
- PostgreSQL
- Additional libraries: djangorestframework, psycopg2-binary, djangorestframework-jwt

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/bookstore-api.git
   cd bookstore-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   Update the database settings in `bookstore/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'yourdbname',
           'USER': 'yourdbuser',
           'PASSWORD': 'yourdbpassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Books
- **GET /api/books/**: Retrieve a list of all books.
- **POST /api/books/**: Add a new book.
- **GET /api/books/{id}/**: Retrieve a specific book by ID.
- **PUT /api/books/{id}/**: Update a specific book by ID.
- **DELETE /api/books/{id}/**: Delete a specific book by ID.

### Customers
- **GET /api/customers/**: Retrieve a list of all customers.
- **POST /api/customers/**: Add a new customer.
- **GET /api/customers/{id}/**: Retrieve a specific customer by ID.
- **PUT /api/customers/{id}/**: Update a specific customer by ID.
- **DELETE /api/customers/{id}/**: Delete a specific customer by ID.

### Orders
- **GET /api/orders/**: Retrieve a list of all orders.
- **POST /api/orders/**: Create a new order.
- **GET /api/orders/{id}/**: Retrieve a specific order by ID.
- **PUT /api/orders/{id}/**: Update a specific order by ID.
- **DELETE /api/orders/{id}/**: Cancel a specific order by ID.

### Authentication
- **POST /api/auth/login/**: Login and retrieve a token.
- **POST /api/auth/register/**: Register a new user.

## Authentication
The API uses JWT for authentication. To access protected routes, include the token in the `Authorization` header:
```
Authorization: Bearer <token>
```

## Request and Response Formats
- **Requests**: JSON
- **Responses**: JSON

### Example
**Request:**
```json
POST /api/books/
{
  "title": "1984",
  "author": "George Orwell",
  "isbn": "9780451524935",
  "price": 9.99,
  "quantity": 100
}
```

**Response:**
```json
{
  "id": 1,
  "title": "1984",
  "author": "George Orwell",
  "isbn": "9780451524935",
  "price": 9.99,
  "quantity": 100,
  "created_at": "2024-06-15T10:00:00",
  "updated_at": "2024-06-15T10:00:00"
}
```

## Error Handling
Errors are returned in the following format:
```json
{
  "error": "Resource not found",
  "message": "The requested resource does not exist.",
  "status_code": 404
}
```

## Examples
### Retrieve All Books
```bash
curl -X GET http://localhost:8000/api/books/
```

### Add a New Book
```bash
curl -X POST http://localhost:8000/api/books/ -H "Content-Type: application/json" -d '{"title": "1984", "author": "George Orwell", "isbn": "9780451524935", "price": 9.99, "quantity": 100}'
```

## Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
