from fastapi import FastAPI
from app.api.state_api import router as state_api

app = FastAPI(title="State Master API")

app.include_router(state_api)
