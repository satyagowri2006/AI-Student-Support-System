from fastapi import APIRouter
from config.database import programs, applications

router = APIRouter()

@router.get("/programs")
def get_programs():

    return list(programs.find({}, {"_id":0}))


@router.post("/apply")
def apply(application: dict):

    applications.insert_one(application)

    return {"message": "Application submitted"}