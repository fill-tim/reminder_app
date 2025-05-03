""" Модуль взаимодействия с таблицей Reminder """
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.models import ReminderModel


class ReminderRepository:

    def __init__(self):
        ...

    async def create(self):
        ...

    async def update(self):
        ...

    async def get_by_id(self):
        ...

    @classmethod
    async def get_all(cls, db: AsyncSession):
        try:
            reminders = await db.execute(
                select(ReminderModel)
            )

            return reminders.scalars().all()

        except Exception as ex:
            raise ex

    async def delete_by_id(self):
        ...
