
# BlogAPI Project

This is a simple Django and Django Rest Framework (DRF) based Blog API. It allows users to perform CRUD operations on blog posts. The project uses Django's built-in ORM for database interactions and supports both SQLite and PostgreSQL databases. It includes authentication via JWT (JSON Web Tokens) to secure the API endpoints.

## Features

- CRUD operations on blog posts.
- JWT Authentication.
- Pagination support for blog posts listing.
- File upload support for blog post images.
- Unit tests for API endpoints.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Django 3.2+
- Django Rest Framework
- Pillow (for image upload functionality)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/blogapi.git
cd blogapi
```

2. Install required Python packages:

```bash
pip install django djangorestframework Pillow
```

3. Apply migrations to create database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

The API will be available at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

### Running Tests

To run the tests, execute:

```bash
python manage.py test
```

## Usage

After starting the development server, you can use tools like Postman or CURL to interact with the API.

### Authentication

- Obtain a JWT token:

```bash
POST /api/token/
```

- Refresh a token:

```bash
POST /api/token/refresh/
```

### CRUD Operations

- Create a blog post:

```bash
POST /api/posts/
```

- Retrieve all blog posts:

```bash
GET /api/posts/
```

- Retrieve a single blog post:

```bash
GET /api/posts/{id}/
```

- Update a blog post:

```bash
PUT /api/posts/{id}/
```

- Delete a blog post:

```bash
DELETE /api/posts/{id}/
```

## Contributing

Contributions are welcome! Please refer to the contributing guidelines for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
