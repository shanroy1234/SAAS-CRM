
from pydantic import BaseModel

class UserIn(BaseModel):
    name:str
    email:str

class LeadIn(BaseModel):
    name:str
    status:str
