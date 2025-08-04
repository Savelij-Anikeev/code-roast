from typing import Optional, List
from abc import ABC, abstractmethod

class Extension(ABC):
    requirements: Optional[List[str]]
    instance = Optional["Extension"]

    @abstractmethod
    async def init(self):
        ...

    @abstractmethod
    def action(self):
        ...