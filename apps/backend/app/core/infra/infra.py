from typing import Optional, List, Any, TypeVar
from abc import ABC, abstractmethod

TDeps = TypeVar("TDeps")

class Infra(ABC):
    name: str
    requirements: Optional[List[str]]
    instance = Optional[Any]

    @abstractmethod
    async def init(self):
        ...

    @abstractmethod
    def action(self, requirements):
        ...