from fastapi import FastAPI
from app.core.database import engine, Base

from app.api.state_api import router as state_api
from app.api.district_api import router as district_api
from app.api.department_api import router as department_api
from app.api.student_api import router as student_api

app = FastAPI(title="Training Master API")

# create all tables
Base.metadata.create_all(bind=engine)

app.include_router(state_api)
app.include_router(district_api)
app.include_router(department_api)
app.include_router(student_api)