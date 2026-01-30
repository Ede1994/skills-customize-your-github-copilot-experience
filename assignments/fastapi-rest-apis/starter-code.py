# FastAPI REST API Starter Code
# Build a Book Management API

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# TODO: Create your FastAPI app instance
app = FastAPI()

# TODO: Define your Book model using Pydantic
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    genre: str

# TODO: Create an in-memory storage for books (dictionary or list)
books = {}

# TODO: Implement the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Management API"}

# TODO: Implement GET endpoint to retrieve all books
# Hint: @app.get("/books")

# TODO: Implement GET endpoint to retrieve a single book by ID
# Hint: @app.get("/books/{book_id}")

# TODO: Implement POST endpoint to create a new book
# Hint: @app.post("/books", status_code=201)

# TODO: Implement PUT endpoint to update a book
# Hint: @app.put("/books/{book_id}")

# TODO: Implement DELETE endpoint to remove a book
# Hint: @app.delete("/books/{book_id}")

# To run this application:
# 1. Install FastAPI and uvicorn: pip install fastapi uvicorn
# 2. Run the server: uvicorn starter-code:app --reload
# 3. Visit http://localhost:8000/docs to see the interactive API documentation
