
from fastapi import FastAPI
app = FastAPI()


BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "math"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "science"},
    {"title": "Title Five", "author": "Author Five", "category": "math"}
]


@app.get("/books")
async def read_all_books():
    return BOOKS      

# Dynamic Path Parameters
@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param:str):
    return {dynamic_param: "This is a dynamic parameter"}

# Querying by Category
@app.get("/books/tittle/{book_title}")
async def read_book_by_title(book_title: str ):
    return [book for book in BOOKS if book["title"].lower() == book_title.lower()]

# post method
@app.post("/books/create_book")
async def create_book(new_book:dict):
    BOOKS.append(new_book)
    return BOOKS


# PUT request → নির্দিষ্ট title অনুযায়ী বই update করা হবে
@app.put("/books/{book_title}")
def update_book(book_title: str, new_author: str, new_category: str):
    """
    book_title (path parameter): কোন বই update হবে তা বোঝায়
    new_author (query parameter): নতুন লেখক
    new_category (query parameter): নতুন category
    """
    for book in BOOKS:
        if book["title"].lower() == book_title.lower():
            # যদি title match করে তাহলে update করো
            book["author"] = new_author
            book["category"] = new_category
            return {"message": "Book updated successfully!", "updated_book": book}

    # যদি বই না পাওয়া যায়
    return {"error": f"Book with title '{book_title}' not found!"}

# DELETE request → নির্দিষ্ট title অনুযায়ী বই delete করা হবে
@app.delete("/books/{book_title}")
def delete_book(book_title: str):
    """
    book_title (path parameter): কোন বই delete করা হবে তা বোঝায়
    """
    for index, book in enumerate(BOOKS):
        if book["title"].lower() == book_title.lower():
            deleted_book = BOOKS.pop(index)  # index অনুযায়ী list থেকে remove
            return {"message": "Book deleted successfully!", "deleted_book": deleted_book}

    # যদি বই না পাওয়া যায়
    return {"error": f"Book with title '{book_title}' not found!"}