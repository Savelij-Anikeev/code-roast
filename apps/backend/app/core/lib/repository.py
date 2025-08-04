from typing import Optional
from abc import ABC, abstractmethod

from .entity import Entity

class Repository(ABC):
    @abstractmethod
    async def get(self) -> Optional[Entity]:
        ...

    @abstractmethod
    async def using(self):
        ...