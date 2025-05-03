""" Модуль для бизнес логики с объектами Reminder """
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.repositories.reminder_repository import ReminderRepository


class ReminderService:

    def __init__(self):
        self.reminder_repository = ReminderRepository()

    async def get_by_id(self):
        ...

    async def get_all(self, db: AsyncSession):
        return self.reminder_repository.get_all(db)

    async def create(self):
        ...

    async def delete_by_id(self):
        ...

    async def update(self):
        ...
