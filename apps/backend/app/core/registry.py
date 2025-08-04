from collections import defaultdict

workflows: dict[str, dict[str, callable]] = defaultdict(dict)

def register_method(
    workflow_name: str,
    method_name: str,
    before_hooks,
    after_hooks
):
    def decorator(fn):
        workflows[workflow_name][method_name] = {
            'method': fn,
            'before_hooks': before_hooks,
            'after_hooks': after_hooks
        }

        return fn
    return decorator