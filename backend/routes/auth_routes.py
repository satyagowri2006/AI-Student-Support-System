from fastapi import APIRouter
from config.database import students

router = APIRouter()

@router.post("/register")
def register(student: dict):

    students.insert_one(student)

    return {"message": "Student registered successfully"}