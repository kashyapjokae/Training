from fastapi import FastAPI
from app.api import department_api

app = FastAPI()


# Include API router
app.include_router(department_api.router)

# Root Route
@app.get("/")
def home():
    return {"message": "Department API is working"}