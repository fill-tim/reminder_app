""" Модуль для модели Reminder """

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.models.base import Base


class ReminderModel(Base):
    __tablename__ = 'reminders'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    reminder_time: Mapped[datetime] = mapped_column(default=datetime.now())
    is_active: Mapped[bool] = mapped_column(default=True)
