from fastapi import FastAPI
from app.api import department

app = FastAPI()

app.include_router(department.router)