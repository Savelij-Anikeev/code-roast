import pytest

from ...core.dispatcher.dispatch import dispatch
from ...core.dispatcher.registry import register_method
from ...core.dispatcher.entities import CallContext, Hook

@pytest.mark.asyncio
async def test_should_throw_error_if_no_calls_passed():
    request = {
        'is_async': False,
        'calls': []
    }

    with pytest.raises(RuntimeError) as error:
        await dispatch(request, None)

    assert 'nothing to call' in str(error.value)

@pytest.mark.asyncio
async def test_should_run_calls_sync_if_handler_registered():
    @register_method('test_workflow', 'test_method')
    def handler(context: CallContext):
        x, y = context.params.values()

        return x + y

    request = {
        'is_async': False,
        'calls': [
            {
                'workflow': 'test_workflow',
                'method': 'test_method',
                'params': {
                    'x': 1,
                    'y': 2
                }
            }
        ]
    }

    [response] = await dispatch(request)

    assert response == 3

@pytest.mark.asyncio
async def test_should_let_before_plugin_change_incoming_params():
    def some_before_hook(context: CallContext):
        context.params['x'] = 5

    @register_method(
        'test_workflow',
        'test_method_1',
        before_hooks=[Hook(caller=some_before_hook)]
    )
    def handler(context: CallContext):
        x, y = context.params.values()

        return x + y

    request = {
        'is_async': False,
        'calls': [
            {
                'workflow': 'test_workflow',
                'method': 'test_method_1',
                'params': {
                    'x': 1,
                    'y': 2
                }
            }
        ]
    }

    [response] = await dispatch(request)

    assert response == 7

@pytest.mark.asyncio
async def test_should_let_after_plugin_change_result():
    def some_before_hook(context: CallContext):
        context.response = 777

    @register_method(
        'test_workflow',
        'test_method_2',
        after_hooks=[Hook(caller=some_before_hook)]
    )
    def handler(context: CallContext):
        x, y = context.params.values()

        return x + y

    request = {
        'is_async': False,
        'calls': [
            {
                'workflow': 'test_workflow',
                'method': 'test_method_2',
                'params': {
                    'x': 1,
                    'y': 2
                }
            }
        ]
    }

    [response] = await dispatch(request)

    assert response == 777