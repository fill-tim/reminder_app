""" Модуль для роутеров Reminder """

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from application.controllers.reminder_controller import ReminderController
from infrastructure.database import DB

reminder_router = APIRouter(prefix="/reminders")

get_session = DB().get_session


@reminder_router.get("/")
async def get_all_reminders(db: AsyncSession = Depends(get_session)):
    return await ReminderController().get_all(db)


@reminder_router.get("/{id}")
def get_all_reminders(id: int, db: AsyncSession = Depends(get_session)):
    return


@reminder_router.post("/")
def create_reminder(db: AsyncSession = Depends(get_session)):
    return


@reminder_router.patch("/")
def update_reminder(db: AsyncSession = Depends(get_session)):
    return


@reminder_router.delete("/{id}")
def delete_reminder(id: int, db: AsyncSession = Depends(get_session)):
    return
