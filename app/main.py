from fastapi import FastAPI
from app.api.state_api import router as state_api
from app.api.district_api import router as district_api
from app.api.department_api import router as department_api
from app.api.fastfood_api import router as fastfood_api
from app.api.subject_api import router as subject_api 
from app.api.student_api import router as student_api
from app.core.base import Base
from app.core.database import engine

app = FastAPI(title="Training Master API")

app.include_router(state_api)
app.include_router(district_api)
app.include_router(department_api)
app.include_router(fastfood_api)
app.include_router(subject_api) 
app.include_router(student_api)

@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
