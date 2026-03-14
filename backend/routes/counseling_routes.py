from fastapi import APIRouter
from config.database import counseling

router = APIRouter()

@router.post("/book-counseling")
def book_counseling(data: dict):

    counseling.insert_one(data)

    return {"message": "Counseling appointment booked"}