""" Модуль главное файла сервиса """

from fastapi import FastAPI

from infrastructure.database import DB
from application import routers

app = FastAPI()


@app.on_event("startup")
async def startup():
    from infrastructure import models
    db = DB()
    await db.connect()
    await db.init_tables()


app.include_router(routers.reminder_router)
