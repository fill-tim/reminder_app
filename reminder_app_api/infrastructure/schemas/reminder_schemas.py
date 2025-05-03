""" Модуль для схем сущности Reminder """

from pydantic import BaseModel
from datetime import datetime


class ReminderBase(BaseModel):
    id: int
    text: str
    reminder_time: datetime
    is_active: bool


class ReminderCreate(BaseModel):
    text: str
    reminder_time: datetime
    is_active: bool
