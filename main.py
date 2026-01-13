
from fastapi import FastAPI
from app.routers import auth, leads, users

app = FastAPI(title="SaaS CRM Application")

app.include_router(auth.router)
app.include_router(leads.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message":"CRM System Running"}
