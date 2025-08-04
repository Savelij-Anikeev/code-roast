from typing import Protocol, Optional, List

class Entity(Protocol):
    events: Optional[List[str]]