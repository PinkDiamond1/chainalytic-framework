from typing import List, Set, Dict, Tuple, Optional
import sys
from jsonrpcserver import async_dispatch as dispatch

EXIT_SERVICE = '__EXIT_SERVICE__'


async def main_dispatcher(websocket, path):
    response = await dispatch(await websocket.recv())
    if response.wanted:
        await websocket.send(str(response))
        if response.result == EXIT_SERVICE:
            print('Terminated service')
            sys.exit()
