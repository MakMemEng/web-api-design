from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class Book(BaseModel):
    isbn: str
    title: str
    authors: List[str]
    price: int


@router.post("/books")
def create_book(book: Book):
    # creating a new book ...
    return {
        "isbn": book.isbn,
        "title": book.title,
        "authors": book.authors,
        "price": book.price,
    }
