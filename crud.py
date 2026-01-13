
from app.models import User,Lead

def create_user(db,data):
    u=User(**data)
    db.add(u);db.commit();db.refresh(u);return u

def create_lead(db,data,uid):
    l=Lead(name=data['name'],status=data['status'],owner_id=uid)
    db.add(l);db.commit();db.refresh(l);return l
