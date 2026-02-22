from fastapi import FastAPI
from app.api import department_api
from app.core.database import engine, Base
from app.Entities.department_model import Department

app = FastAPI()

# Create tables in database
Base.metadata.create_all(bind=engine)

# Include API router
app.include_router(department_api.router)

# Root Route
@app.get("/")
def home():
    return {"message": "Department API is working"}