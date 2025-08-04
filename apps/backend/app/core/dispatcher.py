import asyncio
from typing import Dict, List

from .context import Context

from .registry import workflows

class Dispatcher:
    def call(self, props):
        if not len(props.request.calls):
            raise Exception('nothing to call')

        response = []
        ctx = Context(props)

        if props.request.isAsync:
            response = self._callAsync(props.request.calls)
        else:
            response = self._callSync(props.request.calls)

        return response

    def __callAsync(self, calls):
        return asyncio.gather(map(self.__execute, calls))


    async def __callSync(self, calls):
        result = []

        for call in calls:
            result = await self.__execute(call)

        return result

    async def __execute(self, call, ctx):
        workflow = workflows.get(call.workflow)

        if not workflow:
            raise Exception('workflow not found')

        meta = workflow.get(call.method)

        if not meta.get('method'):
            raise Exception('method not found')

        if len(meta.before_hooks):
            for hook in meta.before_hooks:
                await hook(meta, ctx)

        response = await meta.method(meta, ctx)

        if len(meta.after_hooks):
            for hook in meta.after_hooks:
                await hook(response, meta, ctx)

        return response