from fastapi import APIRouter
from config.database import scholarships

router = APIRouter()

@router.get("/scholarships")
def get_scholarships():

    return list(scholarships.find({}, {"_id":0}))