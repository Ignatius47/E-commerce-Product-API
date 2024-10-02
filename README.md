E-commerce Product API

Overview
This API is designed to manage core e-commerce functionalities such as product management, user authentication, and product search/filter capabilities. Built using Django and Django REST Framework (DRF), it supports full CRUD (Create, Read, Update, Delete) operations and includes role-based access control for secure resource handling.

Features
CRUD Operations: Manage Products, Categories, and Orders.
User Authentication: Token-based authentication for secure access.
Role-Based Access Control: Admin and regular user permissions.
Search and Filter: Search products and filter by category, price, and availability.
Pagination: Handle large datasets efficiently.

Technologies Used
Python 3.x
Django 4.x
Django REST Framework (DRF)
PostgreSQL (for production)
SQLite (for local development)
Lucidchart (for ERD design)

Before setting up the project, make sure you have the following installed:
Python 3.x
Virtual Environment Tool (like venv)
PostgreSQL (or SQLite for local development)
Git
pip for package management

Setup Instructions

1. Clone the Repository
git clone https://github.com/Ignatius47/E-commerce-Product-API.git
cd ecommerce-api

2. Create and Activate a Virtual Environment
# Unix-based systems:
python3 -m venv env
source env/bin/activate

# Windows:
python -m venv env
env\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

4. Database Configuration
In settings.py, configure the database settings:

5. Apply Database Migration
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser
python manage.py createsuperuser

7. Run the Development Server
python manage.py runserver
Your API will be available at http://127.0.0.1:8000/api/.

API Endpoints
Authentication
Login (POST) /api/auth/login/
Register (POST) /api/auth/register/

Products
Create Product (POST) /api/products/ (Admin only)
List Products (GET) /api/products/
Retrieve Product (GET) /api/products/<id>/
Update Product (PUT) /api/products/<id>/ (Admin only)
Delete Product (DELETE) /api/products/<id>/ (Admin only)

Categories
Create Category (POST) /api/categories/ (Admin only)
List Categories (GET) /api/categories/
Retrieve Category (GET) /api/categories/<id>/
Update Category (PUT) /api/categories/<id>/ (Admin only)
Delete Category (DELETE) /api/categories/<id>/ (Admin only)

Orders
Create Order (POST) /api/orders/ (Authenticated users)
List Orders (GET) /api/orders/ (Admin only)
Retrieve Order (GET) /api/orders/<id>/
Update Order (PUT) /api/orders/<id>/ (Admin only)
Delete Order (DELETE) /api/orders/<id>/ (Admin only)

Filtering and Search
Search Products (GET) /api/products/?search=<query>
Filter Products (GET) /api/products/?category=<category_id>

Troubleshooting
Database Issues: Ensure PostgreSQL or SQLite is configured correctly in settings.py.
Static Files Issues: Run python manage.py collectstatic in production.

Contact
For questions or support, feel free to reach out via:

Email: ignatiusx47@gmai.com
GitHub: Ignatius47