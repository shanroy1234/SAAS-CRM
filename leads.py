
from fastapi import APIRouter
from app.database import SessionLocal
from app.crud import create_lead

router=APIRouter(prefix='/leads')

@router.post('/create/{uid}')
def add(uid:int,data:dict):
    db=SessionLocal()
    return create_lead(db,data,uid)
