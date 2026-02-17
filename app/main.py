from fastapi import FastAPI
from app.api.state_api import router as state_api
from app.api.district_api import router as district_api
from app.api.department_api import router as department_api
from app.api.fastfood_api import router as fastfood_api
app = FastAPI(title="Training Master API")

app.include_router(state_api)
app.include_router(district_api)
app.include_router(department_api)
app.include_router(fastfood_api)
