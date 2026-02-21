from fastapi import FastAPI
from app.core.database import engine, Base
from app.Entities import department_model
from app.api import department_api

app = FastAPI()

# Create Tables
Base.metadata.create_all(bind=engine)

# Include Router
app.include_router(department_api.router)