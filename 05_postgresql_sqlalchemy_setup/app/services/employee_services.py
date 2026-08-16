from sqlalchemy.ext.asyncio import AsyncSession
from app.models.employee_models import Employee
from sqlalchemy import select


class EmployeeServices:
    async def get_all_employees(self, db: AsyncSession):
        result = await db.execute(select(Employee))
        employees = result.scalars().all()

        return employees


employee_services = EmployeeServices()
