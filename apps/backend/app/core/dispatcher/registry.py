from collections import defaultdict
from typing import List, Optional

from .entities import MethodData, Hook

workflows: dict[str, dict[str, MethodData]] = defaultdict(dict)

def register_method(
    workflow_name: str,
    method_name: str,
    before_hooks: Optional[List[Hook]] = None,
    after_hooks: Optional[List[Hook]] = None
):
    def decorator(fn):
        workflows[workflow_name][method_name] = MethodData(
            method=fn,
            before_hooks=before_hooks,
            after_hooks=after_hooks
        )

        return fn

    return decorator
