from typing import Optional, List, TypeVar, Generic, Any
from dataclasses import dataclass

@dataclass()
class User:
    id: int
    permissions: int

@dataclass()
class Meta:
    user: Optional[User] = None
    tz: Optional[int] = None

@dataclass()
class Request:
    calls: list
    is_async: bool
    uuid: str

@dataclass()
class Call:
    workflow: str
    method: str
    params: dict | list

@dataclass()
class Context(dict):
    pass

@dataclass()
class Hook:
    caller: callable
    is_async: Optional[bool] = None
    type: Optional[str] = None # after | before

@dataclass()
class MethodData:
    method: callable
    before_hooks: Optional[List[Hook]]
    after_hooks: Optional[List[Hook]]

CallContextParams = TypeVar("CallContextParams")

@dataclass()
class CallContext(Generic[CallContextParams]):
    params: CallContextParams
    infra: dict # TODO:
    context: Optional[Context] = None
    meta: Optional[Meta] = None
    response: Any = None
