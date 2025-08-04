import asyncio
import inspect

from typing import List

from .entities import Context, Call, Meta, CallContext

from .registry import workflows

def run_async(calls: List[Call], meta: Meta):
    return asyncio.gather(*[
        execute_method(call.workflow, call.method, call.params, Context(), meta)
        for call in calls
    ])

async def run_sync(calls: List[Call], meta: Meta):
    context = Context()
    response = []

    for call in calls:
        workflow = call.workflow
        method = call.method
        params = call.params

        call_result = await execute_method(workflow, method, params, context, meta)

        response.append(call_result)

    return response

async def execute_method(workflow, method, params, context, meta):
    workflow_data = workflows.get(workflow)

    if not workflow_data:
        raise RuntimeError(f'there is no workflow called "{workflow}"')

    method_data = workflow_data.get(method)

    if not method_data:
        raise RuntimeError(f'workflow "{workflow}" has no "{workflow}" method')

    context_props = CallContext(
        params=params,
        infra={}, # TODO: extensions
        meta=meta,
        context=context,
        response=None
    )

    if method_data.before_hooks and len(method_data.before_hooks):
        for hook in method_data.before_hooks:
            result = hook.caller(context_props)

            if inspect.isawaitable(result):
                await result

    context_props.response = method_data.method(context_props)

    if inspect.isawaitable(context_props.response):
        context_props.response = await context_props.response

    if method_data.after_hooks and len(method_data.after_hooks):
        for hook in method_data.after_hooks:
            if hook.is_async:
                hook.caller(context_props)
            else:
                result = hook.caller(context_props)

                if inspect.isawaitable(result):
                    await result

    return context_props.response
