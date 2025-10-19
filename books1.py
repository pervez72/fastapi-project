
from ast import List
import stat
from typing import Optional
from fastapi import FastAPI,Body, Query

app = FastAPI()

# Define a Book model 



# Book Class define all attributes
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

# main list of books
BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]



# Endpoint to get all books
@app.get("/books")
async def read_all_books():
    return BOOKS

#noarmally insert new book without validation
# insert new book
@app.post("/books")
async def create_book(new_book_add=Body()):
    BOOKS.append(new_book_add)
    return new_book_add

##============================================================================================
#pydantic model = its a data validation and settings management using python type annotations
from pydantic import BaseModel, Field
class BookModel(BaseModel):
    id: int 
    title: str = Field(..., min_length=3)
    author: str = Field(max_length=20)
    description: str
    rating: int
    published_date: int 

# book creation with pydantic model / insert new book use validation
@app.post("/books/validation")
async def create_book(new_book: BookModel):
    BOOKS.append(new_book)
    return new_book



# Fetch book by id
from fastapi import HTTPException
@app.get("/books/{book_id}",response_model=BookModel)
async def get_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")



# this is bug next solve it later

# from typing import List, Optional
# #filter books by rating
# @app.get("/books/filter", response_model=List[BookModel])
# async def filter_books(rating: Optional[int] = Query(None, ge=1, le=5)):
#     """
#     Filter books by rating.
#     - rating: integer between 1 and 5
#     """
#     if rating is None:
#         return BOOKS  # return all if no rating provided
#     filtered_books = [book for book in BOOKS if book.rating == rating]
#     return filtered_books


# Update book by id
@app.put("/books/{book_id}", response_model=BookModel)
async def update_book(book_id: int, updated_book: BookModel):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            # Update book
            BOOKS[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")


# Delete book by id
@app.delete("/books/{book_id}", response_model=BookModel)
async def delete_book(book_id: int):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            deleted_book = BOOKS.pop(index)
            return deleted_book  # returns full BookModel
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
