
from fastapi import APIRouter,Depends
from app.database import SessionLocal
from app.crud import create_user

router=APIRouter(prefix='/users')

@router.post('/create')
def create(data:dict):
    db=SessionLocal()
    return create_user(db,data)
