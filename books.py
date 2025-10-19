
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

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param:str):
    return {dynamic_param: "This is a dynamic parameter"}
