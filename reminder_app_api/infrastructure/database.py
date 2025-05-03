""" Модуль для настроек подключения с БД """

from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import Config
from infrastructure.models.base import Base


class DB(Config):

    def __init__(self):
        self.database = Database(self.database_url)
        self.engine = create_async_engine(self.database_url, echo=True)

    async def init_tables(self) -> None:
        """ Создаем таблицы """

        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

        except Exception as ex:
            raise ex

    async def get_session(self) -> AsyncSession:
        """ Получение сессии """

        async_session_maker = async_sessionmaker(self.engine, expire_on_commit=False)
        async with async_session_maker() as session:
            yield session

    async def connect(self):
        """ Подключаемся к БД """

        try:
            await self.database.connect()
        except Exception as ex:
            raise ex

    async def disconnect(self):
        """ Отключаемся от БД """
        try:
            await self.database.disconnect()
        except Exception as ex:
            raise ex
