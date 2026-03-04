from fastapi import FastAPI
from app.api.state_api import router as state_api
from app.api.district_api import router as district_api
from app.api.department_api import router as department_api
from app.api.fastfood_api import router as fastfood_api
from app.api.student_api import router as student_api
from app.Entities.student import Student as Student
from app.core.base import Base
from app.core.database import engine
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn: 
     await  conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Training Master API",lifespan=lifespan)

app.include_router(state_api)
app.include_router(district_api)
app.include_router(department_api)
app.include_router(fastfood_api)
app.include_router(student_api)