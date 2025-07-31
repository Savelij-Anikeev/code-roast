from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_db

app = FastAPI()

@app.get("/")
async def healthcheck(db: AsyncSession = Depends(get_db)):
    await db.execute("SELECT 1")

    # pong = await redis_client.ping()

    return {
        "status": "ok",
        "redis": 'pong'
    }