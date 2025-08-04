from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from ..core.protocols.extension import Extension
from ..core.config import settings

class PgExtension(Extension):
    def init(self):
        engine = create_async_engine(
            settings.DATABASE_URL,
            echo=settings.ENV == 'development'
        )
        self.instance = sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def action(self):
        async with self.instance() as connection:
            yield connection
