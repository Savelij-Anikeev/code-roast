from typing import Protocol, Optional, List

class Extension(Protocol):
    requirements: Optional[List["Extension"]]
    instance = Optional["Extension"]

    def init(self):
        ...

    def action(self):
        ...