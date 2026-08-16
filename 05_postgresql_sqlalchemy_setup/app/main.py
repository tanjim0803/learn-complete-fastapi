from fastapi import FastAPI
from app.routers.employee_router import router as employee_router

app = FastAPI()

app.include_router(employee_router)
