from typing import Optional, List
from abc import ABC

class Entity(ABC):
    events: Optional[List[str]]