from fastapi import APIRouter
from config.database import hostel, transport

router = APIRouter()

@router.get("/hostels")
def get_hostels():

    return list(hostel.find({}, {"_id":0}))


@router.get("/transport")
def get_transport():

    return list(transport.find({}, {"_id":0}))