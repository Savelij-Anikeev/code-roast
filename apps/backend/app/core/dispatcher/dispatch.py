from .utils import run_async, run_sync
from .entities import Call, Meta

async def dispatch(request, metadata=None):
    calls = list(map(lambda x: Call(**x), request.get('calls', [])))
    meta = Meta(**metadata) if metadata else None

    if not len(calls):
        raise RuntimeError('nothing to call')
    if request.get('is_async'):
        return await run_async(calls=calls, meta=meta)
    else:
        return await run_sync(calls=calls, meta=meta)
