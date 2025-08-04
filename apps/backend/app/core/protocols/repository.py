from typing import Optional, Protocol

from .entity import Entity

class Repository(Protocol):
    async def get(self) -> Optional[Entity]:
        ...

    async def using(self):
        ...