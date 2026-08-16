from fastapi import APIRouter
from app.database.session import SessionDep
from app.services.employee_services import employee_services

router = APIRouter(prefix="/employee", tags=["Employees"])


@router.get("/")
async def get_employees(db: SessionDep):
    return await employee_services.get_all_employees(db)
