from fastapi import APIRouter
from app.database.session import SessionDep
from app.services.employee_services import employee_services

router = APIRouter(prefix="/employee", tags=["Employees"])


@router.get("/")
async def get_employees(db: SessionDep):
    return await employee_services.get_all_employees(db)


@router.get("/pagination")
async def get_employees_by_pagination(db: SessionDep, page: int, limit: int):
    return await employee_services.get_employees_pagination(db, page, limit)
