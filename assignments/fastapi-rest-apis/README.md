# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern REST APIs using the FastAPI framework in Python. You'll create a fully functional API with multiple endpoints, data validation, and proper HTTP methods while understanding web development concepts.

## 📝 Tasks

### 🛠️ Create a Book Management API

#### Description
Build a RESTful API for managing a collection of books. The API should support creating, reading, updating, and deleting books (CRUD operations) with proper data validation and HTTP status codes.

#### Requirements
Completed program should:

- Create a FastAPI application with at least 4 endpoints (GET, POST, PUT, DELETE)
- Implement a `Book` model using Pydantic with fields: id, title, author, year, and genre
- Store books in a Python dictionary or list (in-memory storage)
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include proper request validation and error handling
- Add a root endpoint (`/`) that returns a welcome message


### 🛠️ Test Your API

#### Description
Test all API endpoints to ensure they work correctly. Document the endpoints and provide example requests and responses.

#### Requirements
Completed program should:

- Successfully start the FastAPI server using `uvicorn`
- Handle GET requests to retrieve all books or a single book by ID
- Accept POST requests to add new books with validation
- Support PUT requests to update existing books
- Process DELETE requests to remove books from the collection
- Return proper error messages for invalid requests (e.g., book not found)
