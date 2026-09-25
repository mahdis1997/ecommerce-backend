# E-commerce Backend

A RESTful e-commerce backend built with **Django**, **Django REST Framework**, and **PostgreSQL**.

This project is being developed as a practical backend project to implement and learn real-world concepts such as REST APIs, authentication, permissions, database relationships, cart management, and external API integration.

## 🚀 Technologies

* Python
* Django
* Django REST Framework
* PostgreSQL
* JWT Authentication
* Git & GitHub
* REST API
* DummyJSON API

## ✨ Features

### Products

* Product CRUD API
* Product listing and detail endpoints
* Pagination
* Admin-only permissions for product management
* Integration with DummyJSON API
* Import external products into PostgreSQL
* Duplicate product prevention

### Authentication & Users

* User registration
* JWT authentication
* Login and token-based authentication
* User permissions
* Admin permissions

### Shopping Cart

* User-specific shopping cart
* One-to-one relationship between users and carts
* Cart items
* Product and quantity management

## 🗂️ Project Structure

```text
ecommerce-backend/
│
├── accounts/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── services.py
│   ├── permissions.py
│   ├── pagination.py
│   └── urls.py
│
├── orders/
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── test.py
├── .gitignore
└── README.md
```

## 🔐 Authentication

The API uses **JWT (JSON Web Token)** authentication.

Users can register and authenticate to access protected endpoints.

Authentication is handled using access and refresh tokens.

## 🛒 Cart Architecture

The shopping cart uses the following database relationships:

```text
User
 │
 │ OneToOne
 ▼
Cart
 │
 │ ForeignKey
 ▼
CartItem
 │
 │ ForeignKey
 ▼
Product
```

Each user has their own cart, and each cart can contain multiple cart items.

## 🌐 External API Integration

The project integrates with **DummyJSON** as an external product API.

External product data is retrieved, transformed, and stored in the local PostgreSQL database.

This demonstrates how a Django backend can consume and process data from third-party APIs.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-backend.git
cd ecommerce-backend
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## 🔗 API Endpoints

### Products

```text
GET     /api/products/
GET     /api/products/<id>/
POST    /api/products/
PUT     /api/products/<id>/
PATCH   /api/products/<id>/
DELETE  /api/products/<id>/
```

### Authentication

```text
POST    /api/register/
POST    /api/token/
POST    /api/token/refresh/
```

> Additional endpoints will be added as the project develops.

## 🧪 Testing

The project includes Django/DRF test files for application components.

API endpoints can also be tested using tools such as:

* Postman
* Django REST Framework Browsable API

## 🛠️ Roadmap

* [x] Product CRUD
* [x] User registration
* [x] JWT authentication
* [x] Permissions
* [x] Generic Views
* [x] ViewSets & Routers
* [x] PostgreSQL integration
* [x] External product API integration
* [x] Product import service
* [x] Shopping cart models
* [x] Shopping cart API
* [x] Order management
* [x] Checkout
* [x] Payment gateway integration
* [ ] Automated tests
* [ ] Docker
* [ ] Deployment

## 📌 Project Status

This project is currently under active development.

The goal is to build a complete and production-oriented e-commerce backend while applying practical backend development concepts with Django REST Framework.
