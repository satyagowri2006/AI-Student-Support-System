from fastapi import APIRouter
from config.database import courses

router = APIRouter()

@router.get("/courses")
def get_courses():

    return list(courses.find({}, {"_id":0}))