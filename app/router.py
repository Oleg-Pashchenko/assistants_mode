import asyncio

from aiohttp import web

from app.core import execute
from app.methods import *

app = web.Application()


async def assistants_handler(request):
    data = await request.json()

    assistant_id = data['assistant_id'],
    api_token = data['api_token']
    question = data['question']
    thread_id = data['thread_id']
    answer = await execute(
        question=question,
        token=api_token,
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    return web.json_response({
        'status': True,
        'answer': {"text": answer[0],
                   'thread_id': answer[1]},
        'execution_time': 0
    })


async def routers():
    app.router.add_post('/', assistants_handler)


asyncio.run(routers())
