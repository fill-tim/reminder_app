""" Модуль контроллеров Reminder """

from domain.services.reminder_service import ReminderService
from sqlalchemy.ext.asyncio import AsyncSession


class ReminderController:

    def __init__(self):
        self.reminder_service = ReminderService()

    async def create(self):
        return self.reminder_service

    async def get_all(self, db: AsyncSession):
        return self.reminder_service.get_all(db, )

    async def get_by_id(self):
        ...

    async def delete_by_id(self):
        ...

    async def update(self):
        ...