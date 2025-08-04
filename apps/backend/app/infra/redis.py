import redis.asyncio as redis

from ..core.lib.extension import Extension
from ..core.config import settings

class RedisExtension(Extension):
    def init(self):
        self.instance = redis.from_url(
        settings.REDIS_URL,
        encoding="utf-8",
        decode_responses=True
    )

    def action(self):
        return self.instance